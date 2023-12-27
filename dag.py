from asyncio import tasks
from nis import cat
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

from cities.sao_paulo import sao_paulo
from cities.df import df
from cities.rio import rio
from cities.curitiba import curitiba
from cities.backups import backup

with DAG("cities",
    start_date=datetime(2022, 9, 16),
    schedule_interval=timedelta(seconds=60),
    catchup=False,
    default_args={
        "email": ["datasetpibic@gmail.com"],
        "email_on_failure": True}
) as dag:
    sp_task = PythonOperator(
        task_id= "sp",
        python_callable=sao_paulo
    )

    df_task = PythonOperator(
    	task_id= "df",
    	python_callable=df
    )

    rio_task = PythonOperator(
    	task_id= "rio",
    	python_callable=rio
    )

    
    curitiba_task = PythonOperator(
    	task_id= "curitiba",
    	python_callable=curitiba
    )

    backup_task = PythonOperator(
        task_id="backup",
        python_callable=backup
    )
    
    sp_task >> rio_task >> curitiba_task >> df_task >> backup_task
