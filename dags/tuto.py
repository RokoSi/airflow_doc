import subprocess
from datetime import datetime
from docker.types import Mount
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.providers.docker.operators.docker import DockerOperator
from airflow.operators.bash import BashOperator
from airflow.providers.docker.operators.docker import DockerOperator


args = {
    'owner': 'chernyshev',
    'depends_on_past': False,
    'start_date': datetime(2023, 7, 30),
    'retries': 1,

    # 'provide_context': True
}

with DAG('test_de', description='test1', schedule_interval='*/1 * * * *', catchup=False,
         default_args=args) as dag:

    # def run_get_url():
    #     """Функция для запуска скрипта get_url."""
    #     command = "source /var/project/get_url/venv/bin/activate && python /var/project/get_url/main.py"
    #     subprocess.run(["/bin/bash", "-c", command], check=True)
    #
    # def run_db_project():
    #     """Функция для запуска скрипта db_project."""
    #     command = "source /var/project/db_source/venv/bin/activate && python /var/project/db_source/main.py"
    #     subprocess.run(["/bin/bash", "-c", command], check=True)
    #
    # task1 = PythonOperator(
    #     task_id='task1',
    #     python_callable=run_db_project,
    #     dag = dag
    # )
    # task2 = PythonOperator(
    #     task_id='task2',
    #     python_callable=run_db_project,
    #     dag = dag
    # )
    # task1 >> task2

#     mount = Mount(
#         source='C:/Users/chernyshev/PycharmProjects/project_one_to_many/src/get_url',
#         target='/var/get_url',
#         type='bind'
#     )
#     mount1 = Mount(
#         source='C:/Users/chernyshev/PycharmProjects/project_one_to_many/src/get_url',
#         target='/var/db_source',
#         type='bind'
#     )
# #/project
#     #cd /var/get_url && python -m venv venv && source venv/bin/activate && pip install poetry && poetry install --no-root && poetry update &&
#     run_get_url = DockerOperator(
#         task_id='run_get_url',
#         image='python:3.11.6',
#         api_version='auto',
#         auto_remove=True,
#         command='bash -c " python /var/get_url/main.py"',
#         docker_url='unix://var/run/docker.sock',
#         network_mode='bridge',
#         mounts=[mount],
#         #volumes=['/c/Users/chernyshev/PycharmProjects/project_one_to_many/src/get_url:/var/project/get_url'],
#         environment={
#             'URL': 'https://randomuser.me/api/?results=',
#             'USER_KAFKA': 'aGFybWxlc3MtbGxhbWEtMTA5NTUkSWlsftAT5bb2G5AxTAXsG48EcNi8Pk20sDU',
#             'PASSWORD_KAFKA': 'YzI5N2JhYzQtZGJjMi00YjJmLThjOTQtMTEwNzhiZjQ3MmNm',
#             'TOPIC': 'test_msg',
#
#         },
#     )
# #cd /var/db_source && python -m venv venv && source venv/bin/activate && pip install poetry && poetry install --no-root && poetry update && poetry add confluent_kafka && poetry update &&
#     run_db_project = DockerOperator(
#         task_id='run_db_project',
#         image='python:3.11.6',
#         api_version='auto',
#         auto_remove=True,
#         command='bash -c " python /var/db_source/main.py"',
#         #volumes=['/c/Users/chernyshev/PycharmProjects/project_one_to_many/src/db_source:/var/project/db_source'],
#         docker_url='unix://var/run/docker.sock',
#         network_mode='bridge',
#         mounts=[mount1],
#         environment={
#             'HOST': 'db',
#             'DB': 'de_projects',
#             'USER': 'admin',
#             'PASSWORD': 'password',
#             'PORT': '5432',
#             'USER_KAFKA': 'aGFybWxlc3MtbGxhbWEtMTA5NTUkSWlsftAT5bb2G5AxTAXsG48EcNi8Pk20sDU',
#             'PASSWORD_KAFKA': 'YzI5N2JhYzQtZGJjMi00YjJmLThjOTQtMTEwNzhiZjQ3MmNm',
#             'TOPIC': 'test_msg'
#         },
#     )
#
#     run_get_url >> run_db_project

    run_get_url = DockerOperator(
            task_id='run_get_url',
            image='python:3.11.6',
            api_version='auto',
            auto_remove=True,
            command='bash -c " python /var/get_url/main.py "',
            docker_url='unix://var/run/docker.sock',
            network_mode='bridge',
            mounts=[Mount(source='/c/Users/chernyshev/PycharmProjects/project_one_to_many/src/get_url',target='/var/get_url',type='bind')],
            #volumes=['/c/Users/chernyshev/PycharmProjects/project_one_to_many/src/get_url:/var/project/get_url'],
            environment={
                'URL': 'https://randomuser.me/api/?results=',
                'USER_KAFKA': 'aGFybWxlc3MtbGxhbWEtMTA5NTUkSWlsftAT5bb2G5AxTAXsG48EcNi8Pk20sDU',
                'PASSWORD_KAFKA': 'YzI5N2JhYzQtZGJjMi00YjJmLThjOTQtMTEwNzhiZjQ3MmNm',
                'TOPIC': 'test_msg',

            },)

    run_get_url