import logging
from datetime import datetime
from airflow import DAG
from airflow.models import Variable
from airflow.providers.docker.operators.docker import DockerOperator

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)

# Консольный обработчик для вывода логов в стандартный вывод
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
formatter = logging.Formatter("%(asctime)s - %(message)s", "%d/%m/%Y %I:%M:%S %p")
console_handler.setFormatter(formatter)

# Добавление обработчика к логгеру
log.addHandler(console_handler)

args = {
    'owner': 'chernyshev',
    'depends_on_past': False,
    'start_date': datetime(2023, 7, 30),
    'retries': 1,

    # 'provide_context': True
}
unvdf = {
            'host': Variable.get("HOST"),
            'db': Variable.get("DB"),
            'user': Variable.get("USER"),
            'password': Variable.get("PASSWORD"),
            'port': Variable.get("PORT"),
            'user_kafka': Variable.get("USER_KAFKA"),
            'password_kafka': Variable.get("PASSWORD_KAFKA"),
            'topic': Variable.get("TOPIC"),

        }

print("1!!!!!!!!!", unvdf)
with DAG('test_de', description='test1', schedule_interval='*/1 * * * *', catchup=False,
         default_args=args) as dag:
    run_get_url_container = DockerOperator(
        task_id='run_get_url_container',
        image='get_url_image:1.0.0',
        command='python ./src/main.py',  # Replace with the command you need
        docker_url='unix://var/run/docker.sock',
        network_mode='app-network',
        mount_tmp_dir=False,
        # auto_remove=True,
        environment={
            'url': Variable.get("URL"),
            'user_kafka': Variable.get("USER_KAFKA"),
            'password_kafka': Variable.get("PASSWORD_KAFKA"),
            'topic': Variable.get("TOPIC"),
        }
    )
    run_db_source_container = DockerOperator(
        task_id='run_db_source_container',
        image='db_source_image:1.0.0',
        command='python ./src/main.py',  # Replace with the command you need
        docker_url='unix://var/run/docker.sock',
        network_mode='app-network',
        mount_tmp_dir=False,
        # auto_remove=True,
        environment={
            'host': Variable.get("HOST"),
            'db': Variable.get("DB"),
            'user': Variable.get("USER"),
            'password': Variable.get("PASSWORD"),
            'port': Variable.get("PORT"),
            'user_kafka': Variable.get("USER_KAFKA"),
            'password_kafka': Variable.get("PASSWORD_KAFKA"),
            'topic': Variable.get("TOPIC"),

        }
    )
    run_get_url_container >> run_db_source_container
