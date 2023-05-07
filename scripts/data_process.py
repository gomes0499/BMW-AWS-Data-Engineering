import boto3
import os


def start_glue_job(job_name):
    glue = boto3.client(
        "glue",
        region_name=os.environ.get("AWS_REGION"),
        aws_access_key_id=os.environ.get("AWS_ACCESS_KEY_ID"),
        aws_secret_access_key=os.environ.get("AWS_SECRET_ACCESS_KEY"),
    )

    job_run = glue.start_job_run(JobName=job_name)

    return job_run["JobRunId"]


job_name = "glue-spark-job"
job_run_id = start_glue_job(job_name)
print(f"Started Glue job {job_name} with JobRunId: {job_run_id}")
