CREATE TABLE AAAA_SERENA_TEST.AUDIT.ETL_JOB_STATUS (
 JOB_ID NUMBER NOT NULL PRIMARY KEY
     COMMENT 'Unique job id.',
 JOB_START_TS TIMESTAMP_LTZ(3) NOT NULL
     COMMENT 'Timestamp when the job started.',
 JOB_END_TS TIMESTAMP_LTZ(3)
     COMMENT 'Timestamp when the job finished.',
 SCHEMA_NAME VARCHAR(50) NOT NULL
     COMMENT 'Job target table schema name.',
 TABLE_NAME VARCHAR(50) NOT NULL
     COMMENT 'Job target table name.',
 JOB_TYPE VARCHAR(20) NOT NULL
     COMMENT 'Job type, such as INGESTION, DATAMART, ANALYTICS, etc.',
 DATA_FILE_URL VARCHAR(150)
     COMMENT 'URL of the source data file for the job (typically INGESTION job).',
 DAG_ID VARCHAR(100) NOT NULL
     COMMENT 'Id of the Airflow DAG responsible for running the job.',
 RUN_EXEC_DATE DATE NOT NULL
     COMMENT 'Airflow DAG execution date.',
 JOB_STATUS VARCHAR(20) NOT NULL
     COMMENT 'Job status, such as RUNNING, SUCCESS, FAILURE.',
 RECS_PARSED NUMBER NOT NULL
     COMMENT 'Number of records parsed by the job, 0 if not relevant.',
 RECS_STAGED NUMBER NOT NULL
     COMMENT 'Number of records staged by the job, 0 if not relevant.',
 RECS_INSERTED NUMBER NOT NULL
     COMMENT 'Number of records inserted by the job into the target table.',
 RECS_UPDATED NUMBER NOT NULL
     COMMENT 'Number of records updated by the job in the target table.',
 RECS_DELETED NUMBER NOT NULL
     COMMENT 'Number of records deleted by the job from the target table.',
 FAILURE_REASON VARCHAR(1024)
     COMMENT 'Failure reason description for a FAILED job.'
)
 COMMENT = 'ETL job status.'
;
CREATE OR REPLACE AAAA_SERENA_TEST.AUDIT.SEQUENCE ETL_JOB_ID_SEQ START = 1 INCREMENT = 1;
