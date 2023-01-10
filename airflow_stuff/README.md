#### Useful commands:
```
airflow run;
airflow dag_state;
airflow list_dags;
airflow task_state;
airflow test;
```


#### Test task
`airflow tasks test DAG_ID TASK_ID 2022-01-01`
e.g.
`airflow tasks test forex_data_pipeline saving_rates 2022-01-01`

