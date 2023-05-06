from prefect import task, Flow
import subprocess

@task
def run_data_ingestion():
    subprocess.run(["python", "data-ingestion.py"])
    print("Data ingestion script executed.")

@task
def run_data_process():
    subprocess.run(["python", "data-process.py"])
    print("Data process script executed.")

with Flow("DataPipeline") as flow:
    data_ingestion_task = run_data_ingestion()
    data_process_task = run_data_process()
    data_process_task.set_upstream(data_ingestion_task)

# Register the flow with Prefect
flow.register("DataPipeline")
