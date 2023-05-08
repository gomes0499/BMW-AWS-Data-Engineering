from prefect import task, Flow
from prefect_email import EmailServerCredentials, email_send_message
from prefect.context import get_run_context
import subprocess


@task
def run_kinesis_data_ingestion():
    subprocess.run(["python", "data_ingestion.py"])
    print("Data ingestion executed successfully")


@task
def run_data_quality_validation_raw():
    subprocess.run(["python", "data_quality_raw_trigger.py"])
    print("Data validation for data lake raw zone executed successfully")


@task
def run_spark_data_process():
    subprocess.run(["python", "data_process.py"])
    print("Spark process executed successfully")


@task
def run_data_quality_validation_processed():
    subprocess.run(["python", "data_quality_processed_trigger.py"])
    print("Data validation for data lake processed zone executed successfully")


@task
def run_create_athena_table():
    subprocess.run(["python", "athena.py"])
    print("Athena table created successfully")


def notify_exc_by_email(exc):
    context = get_run_context()
    flow_run_name = context.flow_run.name
    email_server_credentials = EmailServerCredentials.load("notify-pipeline-email")
    email_send_message(
        email_server_credentials=email_server_credentials,
        subject=f"Flow run {flow_run_name!r} failed",
        msg=f"Flow run {flow_run_name!r} failed due to {exc}.",
        email_to=email_server_credentials.username,
    )


@Flow
def pipeline():
    try:
        print("data pipeline executed successfully!")
        run_kinesis_data_ingestion()
        run_data_quality_validation_raw()
        run_spark_data_process()
        run_data_quality_validation_processed()
        run_create_athena_table()
    except Exception as exc:
        notify_exc_by_email(exc)
        raise


# Register the flow with Prefect
print(pipeline())
