# Vars for S3 Module
bucket_name = "wu10-datalake"
region      = "us-east-1"

# Vars for Glue
glue_job_name                   = "glue-spark-job"
glue_service_role_arn           = "arn:aws:iam::222498481656:role/data_engineer_services"
glue_version                    = "3.0"

# Vars for Kinesis
kinesis_stream_name        = "wu10-kinesis-stream"
kinesis_stream_shard_count = 1
kinesis_firehose_name      = "wu10-kinesis-firehose"
s3_bucket_prefix           = "raw/"
kinesis_buffer_interval    = 60
role_arn                   = "arn:aws:iam::222498481656:role/data_engineer_services"

