## Install Local Airflow Step : 

```shell
% brew install pythonprint 
% python get-pip.py
% pip --version

% pip install virtualenv
% virtualenv -p python venv

(venv) % mkdir airflow && cd airflow
(venv) % pip install apache-airflow

(venv) % pwd
/Users/<username>/airflow/airflow
(venv) % export AIRFLOW_HOME=/Users/<userid>/airflow/airflow


(venv) % airflow users create \
      --role Admin \
      --username admin \
      --email admin \
      --firstname admin \
      --lastname admin \
      --password admin


(venv) % airflow db init

(venv) % airflow users list

% airflow scheduler

(venv) % export AIRFLOW_HOME=/Users/<userid>/airflow/airflow
(venv) % airflow webserver

```


## Deploy Dag to local environment 

Copy dags/* to AIRFLOW_HOME/dags, you can see different folders :  dags, logs 
Everything can be configured in ``airflow.cfg``

```commandline
.
├── airflow
│   ├── airflow-webserver.err
│   ├── airflow-webserver.log
│   ├── airflow-webserver.out
│   ├── airflow-webserver.pid
│   ├── airflow.cfg
│   ├── airflow.db
│   ├── dags
│   │   ├── __pycache__
│   │   │   └── testdag.cpython-39.pyc
│   │   ├── common
│   │   │   ├── __init__.py
│   │   │   ├── __pycache__
│   │   │   │   ├── __init__.cpython-39.pyc
│   │   │   │   ├── _etl_job.cpython-39.pyc
│   │   │   │   └── snowflake_utility.cpython-39.pyc
│   │   │   ├── _etl_job.py
│   │   │   └── snowflake_utility.py
│   │   └── testdag.py
│   ├── logs
│   │   ├── dag_id=etl_dag
│   │   │   ├── run_id=manual__2023-05-04T16:39:22.025675+00:00
│   │   │   │   └── task_id=execute_insert_job
│   │   │   │       └── attempt=1.log
│   │   │   └── run_id=manual__2023-05-04T16:44:11.597951+00:00
│   │   │       ├── task_id=execute_etl_error_job
│   │   │       │   └── attempt=1.log
│   │   │       ├── task_id=execute_insert_job
│   │   │       │   └── attempt=1.log
│   │   │       └── task_id=execute_update_job
│   │   │           └── attempt=1.log
│   │   ├── dag_processor_manager
│   │   │   └── dag_processor_manager.log
│   │   └── scheduler
│   │       ├── 2023-05-02
│   │       │   └── native_dags
│   │       │       └── example_dags
│   │       │           ├── example_bash_operator.py.log
│   │       │           ├── example_branch_datetime_operator.py.log
│   │       │           ├── example_branch_day_of_week_operator.py.log
│   │       │           ├── example_branch_labels.py.log
│   │       │           ├── example_branch_operator.py.log
│   │       │           ├── example_branch_operator_decorator.py.log
│   │       │           ├── example_branch_python_dop_operator_3.py.log
│   │       │           ├── example_complex.py.log
│   │       │           ├── example_dag_decorator.py.log
│   │       │           ├── example_datasets.py.log
│   │       │           ├── example_dynamic_task_mapping.py.log
│   │       │           ├── example_external_task_marker_dag.py.log
│   │       │           ├── example_kubernetes_executor.py.log
│   │       │           ├── example_latest_only.py.log
│   │       │           ├── example_latest_only_with_trigger.py.log
│   │       │           ├── example_local_kubernetes_executor.py.log
│   │       │           ├── example_nested_branch_dag.py.log
│   │       │           ├── example_params_trigger_ui.py.log
│   │       │           ├── example_params_ui_tutorial.py.log
│   │       │           ├── example_passing_params_via_test_command.py.log
│   │       │           ├── example_python_operator.py.log
│   │       │           ├── example_sensor_decorator.py.log
│   │       │           ├── example_sensors.py.log
│   │       │           ├── example_setup_teardown.py.log
│   │       │           ├── example_setup_teardown_taskflow.py.log
│   │       │           ├── example_short_circuit_decorator.py.log
│   │       │           ├── example_short_circuit_operator.py.log
│   │       │           ├── example_skip_dag.py.log
│   │       │           ├── example_sla_dag.py.log
│   │       │           ├── example_subdag_operator.py.log
│   │       │           ├── example_task_group.py.log
│   │       │           ├── example_task_group_decorator.py.log
│   │       │           ├── example_time_delta_sensor_async.py.log
│   │       │           ├── example_trigger_controller_dag.py.log
│   │       │           ├── example_trigger_target_dag.py.log
│   │       │           ├── example_xcom.py.log
│   │       │           ├── example_xcomargs.py.log
│   │       │           ├── plugins
│   │       │           │   ├── event_listener.py.log
│   │       │           │   ├── listener_plugin.py.log
│   │       │           │   └── workday.py.log
│   │       │           ├── subdags
│   │       │           │   └── subdag.py.log
│   │       │           ├── tutorial.py.log
│   │       │           ├── tutorial_dag.py.log
│   │       │           ├── tutorial_taskflow_api.py.log
│   │       │           └── tutorial_taskflow_api_virtualenv.py.log
│   │       ├── 2023-05-04
│   │       │   ├── native_dags
│   │       │   │   └── example_dags
│   │       │   │       ├── example_bash_operator.py.log
│   │       │   │       ├── example_branch_datetime_operator.py.log
│   │       │   │       ├── example_branch_day_of_week_operator.py.log
│   │       │   │       ├── example_branch_labels.py.log
│   │       │   │       ├── example_branch_operator.py.log
│   │       │   │       ├── example_branch_operator_decorator.py.log
│   │       │   │       ├── example_branch_python_dop_operator_3.py.log
│   │       │   │       ├── example_complex.py.log
│   │       │   │       ├── example_dag_decorator.py.log
│   │       │   │       ├── example_datasets.py.log
│   │       │   │       ├── example_dynamic_task_mapping.py.log
│   │       │   │       ├── example_external_task_marker_dag.py.log
│   │       │   │       ├── example_kubernetes_executor.py.log
│   │       │   │       ├── example_latest_only.py.log
│   │       │   │       ├── example_latest_only_with_trigger.py.log
│   │       │   │       ├── example_local_kubernetes_executor.py.log
│   │       │   │       ├── example_nested_branch_dag.py.log
│   │       │   │       ├── example_params_trigger_ui.py.log
│   │       │   │       ├── example_params_ui_tutorial.py.log
│   │       │   │       ├── example_passing_params_via_test_command.py.log
│   │       │   │       ├── example_python_operator.py.log
│   │       │   │       ├── example_sensor_decorator.py.log
│   │       │   │       ├── example_sensors.py.log
│   │       │   │       ├── example_setup_teardown.py.log
│   │       │   │       ├── example_setup_teardown_taskflow.py.log
│   │       │   │       ├── example_short_circuit_decorator.py.log
│   │       │   │       ├── example_short_circuit_operator.py.log
│   │       │   │       ├── example_skip_dag.py.log
│   │       │   │       ├── example_sla_dag.py.log
│   │       │   │       ├── example_subdag_operator.py.log
│   │       │   │       ├── example_task_group.py.log
│   │       │   │       ├── example_task_group_decorator.py.log
│   │       │   │       ├── example_time_delta_sensor_async.py.log
│   │       │   │       ├── example_trigger_controller_dag.py.log
│   │       │   │       ├── example_trigger_target_dag.py.log
│   │       │   │       ├── example_xcom.py.log
│   │       │   │       ├── example_xcomargs.py.log
│   │       │   │       ├── plugins
│   │       │   │       │   ├── event_listener.py.log
│   │       │   │       │   ├── listener_plugin.py.log
│   │       │   │       │   └── workday.py.log
│   │       │   │       ├── subdags
│   │       │   │       │   └── subdag.py.log
│   │       │   │       ├── tutorial.py.log
│   │       │   │       ├── tutorial_dag.py.log
│   │       │   │       ├── tutorial_taskflow_api.py.log
│   │       │   │       └── tutorial_taskflow_api_virtualenv.py.log
│   │       │   └── testdag.py.log
│   │       ├── 2023-05-05
│   │       │   └── testdag.py.log
│   │       ├── 2023-05-06
│   │       │   └── testdag.py.log
│   │       ├── 2023-05-07
│   │       │   └── testdag.py.log
│   │       ├── 2023-05-08
│   │       │   └── testdag.py.log
│   │       ├── 2023-05-09
│   │       │   └── testdag.py.log
│   │       ├── 2023-05-10
│   │       │   └── testdag.py.log
│   │       ├── 2023-05-11
│   │       │   └── testdag.py.log
│   │       ├── 2023-05-12
│   │       │   └── testdag.py.log
│   │       └── latest -> /Users/sgong/airflow2/airflow/logs/scheduler/2023-05-12
│   └── webserver_config.py
├── airflow.cfg
├── logs
│   └── scheduler
│       ├── 2023-05-02
│       └── latest -> /Users/sgong/airflow2/logs/scheduler/2023-05-02
└── webserver_config.py
```

## Add your snowflake config if you want to recreate the pipeline 

in your dag python script testdag.py