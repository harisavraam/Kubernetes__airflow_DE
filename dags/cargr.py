from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'harisavraam.com',
    'start_date': datetime(2024, 1, 25),
    'catchup': False
}

dag = DAG(
    'cargr',
    default_args = default_args,
    schedule=timedelta(days=1)
)

t1 = BashOperator(
    task_id = 'hello_world',
    bash_command='echo "Hello World"',
    dag = dag
)

t2 = BashOperator(
    task_id = 'hello_dml',
    bash_command='echo "Hello Data Mastery Lab"',
    dag = dag
)

t1 >> t2