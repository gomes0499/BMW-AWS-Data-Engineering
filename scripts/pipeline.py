from prefect import task, Flow
import subprocess


@task
def run_data_ingestion():
    subprocess.run(["python", "data_ingestion.py"])
    print("Data ingestion executed successfully")


@task
def run_data_process():
    subprocess.run(["python", "data_process.py"])
    print("Data process executed successfully")


@task
def run_athena_table():
    subprocess.run(["python", "athena.py"])
    print("Athena table executed successfully")


@Flow
def pipeline():
    print("data pipeline executed successfully!")
    run_data_ingestion()
    run_data_process()
    run_athena_table()


# Register the flow with Prefect
print(pipeline())
