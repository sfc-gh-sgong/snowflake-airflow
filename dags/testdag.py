from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
import logging
from common._etl_job import _ETL_JOB
from common.snowflake_utility import *


default_args = {
    'owner': 'airflow',
    'provide_context': True,
    'retries': 0
}


dag = DAG(
    'etl_dag',
    default_args=default_args,
    max_active_runs=1,
    catchup=False,
    start_date=datetime.now()
)

params = {'snowflake_user': '',
          'account': '',
          'password': '',
          'warehouse': '',
          'database': '',
          'schema': '',
          'snowflake_role': ''}

snowflake_cur = SnowflakeCursor(params)


def etl_error_transformation(**kwargs):
    try:
        print("Start ETL Job")
        sql1 = "insert into AAAA_SERENA_TEST.AUDIT.test_insert select uniform(1, 100, random()),current_timestamp )"
        job = _ETL_JOB(snowflake_cur, 'test_insert', 'audit', 'etl_dag', sql1)
        job._etl_job()

    except Exception as err:

        raise (err)


def etl_insert_transformation(**kwargs):
    try:
        print("Start ETL Job")
        sql1 = "INSERT INTO  AAAA_SERENA_TEST.AUDIT.test_insert VALUES ( 200 , current_timestamp())"
        job = _ETL_JOB(snowflake_cur, 'test_insert', 'audit', 'etl_dag', sql1)
        job._etl_job()

    except Exception as err:

        raise (err)


# def etl_copy_transformation(**kwargs):
#     try:
#         print("Start ETL Job")
#         sql1 = "COPY into AAAA_SERENA_TEST.AUDIT.test_insert from @INGESTION_STAGE/EDW_SmartHome_Objects_Phase2/dbo/vw_DimAgent_incr file_format = (format_name = INGESTION_FILE_FORMAT) FORCE = TRUE"
#         job = _ETL_JOB(snowflake_cur, 'dimagent', 'audit', 'etl_dag', sql1)
#         job._etl_job()
#
#     except Exception as err:
#
#         raise (err)


def etl_update_transformation(**kwargs):
    try:
        print("Start ETL Job")
        sql1 = "UPDATE AAAA_SERENA_TEST.AUDIT.test_insert SET INSERT_DATETIME = NULL WHERE ID = 200"
        job = _ETL_JOB(snowflake_cur, 'test_insert', 'audit', 'etl_dag', sql1)
        job._etl_job()

    except Exception as err:

        logging.info(err)


error_task = PythonOperator(
    task_id='execute_etl_error_job',
    python_callable=etl_error_transformation,
    provide_context=True,
    dag=dag
)

# copy_task = PythonOperator(
#     task_id='execute_etl_copy_job',
#     python_callable=etl_copy_transformation,
#     provide_context=True,
#     dag=dag
# )

insert_task = PythonOperator(
    task_id='execute_insert_job',
    python_callable=etl_insert_transformation,
    provide_context=True,
    dag=dag
)

update_task = PythonOperator(
    task_id='execute_update_job',
    python_callable=etl_update_transformation,
    provide_context=True,
    dag=dag
)

insert_task >> update_task >> error_task