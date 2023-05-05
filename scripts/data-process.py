import boto3


def start_glue_job(job_name):
    glue = boto3.client("glue", region_name="us-east-1")

    job_run = glue.start_job_run(JobName=job_name)

    return job_run["JobRunId"]


job_name = "glue-spark-job"
job_run_id = start_glue_job(job_name)
print(f"Started Glue job {job_name} with JobRunId: {job_run_id}")
