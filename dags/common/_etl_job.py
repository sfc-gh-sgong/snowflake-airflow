from typing import Mapping, Sequence, Any, Optional
import logging


def _get_counts_from_result(
        cur,
        result_row: Sequence[Any],
        job_result: Mapping[str, int]
) -> None:
    """Get insert/update/delete counts from SQL statement result."""

    for col_ind, col_val in enumerate(result_row):
        col_desc = cur.cur.description[col_ind][0]
        if col_desc == 'number of rows inserted':
            job_result['recs_inserted'] = job_result.get('recs_inserted', 0) + col_val
        elif col_desc == 'number of rows updated':
            job_result['recs_updated'] = job_result.get('recs_updated', 0) + col_val
        if col_desc == 'number of rows deleted':
            job_result['recs_deleted'] = job_result.get('recs_deleted', 0) + col_val

    if 'recs_deleted' not in job_result:
        job_result['recs_deleted'] = 0

    if 'recs_updated' not in job_result:
        job_result['recs_updated'] = 0

    if 'recs_inserted' not in job_result:
        job_result['recs_inserted'] = 0

    job_result['recs_parsed']=0


def _get_copy_counts_from_result(
        result: Sequence[Any],
        job_result: Mapping[str, int]
):
    if len(result) == 1 and len(result[0]) == 1:
        logging.info("no new files loaded")
        job_result['recs_parsed']=0
    else:
        if 'data_file_urls' not in job_result:
            job_result['data_file_urls'] = []
            job_result['recs_parsed'] = 0
            for row in result:
                job_result['data_file_urls'].append(('STAGE', row[0]))
                job_result['recs_parsed'] += int(row[2])
    job_result['recs_inserted']=0
    job_result['recs_updated']=0
    job_result['recs_deleted']=0

    return


def _str_sql_lit(val: Optional[str]) -> str:
    """Make SQL string literal expression from the specified string value."""
    return "'" + val.replace("'", "''") + "'" if val is not None else 'NULL'


class _ETL_JOB:

    def __init__(self, cur,table_name,schema_name,dag_id,sql):
        self.etl_query = sql
        self.job_result= {}
        self.table_name=table_name
        self.schema_name=schema_name
        self.dag_id = dag_id
        self.cur = cur


    def _etl_job(self):
        # allocate job id
        try:
            sql = ('SELECT AAAA_SERENA_TEST.AUDIT.ETL_JOB_ID_SEQ.NEXTVAL FROM DUAL')
            self.cur.execute(sql)
            job_id = self.cur.fetch_single_element()
            logging.info("job_id is %s", (job_id))

            sql = f''' INSERT INTO AAAA_SERENA_TEST.AUDIT.ETL_JOB_STATUS (
                              JOB_ID,
                              JOB_START_TS,
                              SCHEMA_NAME,
                              TABLE_NAME,
                              JOB_TYPE,
                              DAG_ID,
                              DAG_RUN_EXEC_DATE,
                              JOB_STATUS,
                              RECS_PARSED,
                              RECS_STAGED,
                              RECS_INSERTED,
                              RECS_UPDATED,
                              RECS_DELETED) VALUES 
                              ({job_id}, current_timestamp,
                              '{self.schema_name}', 
                              '{self.table_name}', 
                              'Ingestion',
                              '{self.dag_id}',Current_date, 'RUNNING', 0, 0, 0, 0, 0)
                              '''
            logging.info("executing SQL: %s", sql)
            self.cur.execute(sql)

        except Exception as err:
            raise err

        try:
            logging.info("executing job logic")
            self.cur.execute(self.etl_query)
            res = self.cur.fetchall()

            if "copy" in self.etl_query.lower():
                _get_copy_counts_from_result(res, self.job_result)
            else:
                _get_counts_from_result(self.cur, res[0], self.job_result)

            sql = (f"UPDATE AAAA_SERENA_TEST.AUDIT.ETL_JOB_STATUS"
                f" SET JOB_END_TS = CURRENT_TIMESTAMP()"
                f", JOB_STATUS = 'SUCCESS'"
                f", RECS_PARSED = {self.job_result['recs_parsed']}"
                f", RECS_INSERTED = {self.job_result['recs_inserted']}"
                f", RECS_UPDATED = {self.job_result['recs_updated']}"
                f", RECS_DELETED = {self.job_result['recs_deleted']}"
                f" WHERE JOB_ID = {job_id}"
            )

            print(sql)
            logging.info("executing SQL: %s", sql)
            self.cur.execute(sql)

        # error executing the job
        except Exception as err:

            sql = (f"UPDATE AAAA_SERENA_TEST.AUDIT.ETL_JOB_STATUS"
                    f" SET JOB_END_TS = CURRENT_TIMESTAMP()"
                    f", JOB_STATUS = 'FAILURE'"
                    f", FAILURE_REASON = {_str_sql_lit(type(err).__name__ + ': ' + str(err))}"
                    f" WHERE JOB_ID = {job_id}"
                )
            logging.info("executing SQL: %s", sql)
            self.cur.execute(sql)
            logging.info("update the execution errors")
            # Close the Connection
            self.cur.close()
            raise err