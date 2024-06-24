from airflow import DAG
from datetime import timedelta, datetime

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date':datetime(2024,6,2),
    'email': ['sjitbh121993@gmail.com'],
    'email_on_failure':False,
    'email_on_retry':False,
    'retries':2,
    'retry_delay':timedelta(seconds=15)
}

with DAG('my_dag', default_args=default_args, schedule_interval='@weekly', catchup=False) as dag:
    