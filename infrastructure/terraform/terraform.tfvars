# Vars for S3 Module
bucket_name = "wu10-datalake"
region      = "us-east-1"

# Vars for Glue
glue_job_name         = "glue-spark-job"
glue_service_role_arn = "arn:aws:iam::222498481656:role/data_engineer_services"
glue_script_name      = "spark-job.py"