# S3
module "s3" {
  source = "./modules/S3"

  bucket_name = var.bucket_name
  region      = var.region
}

# Glue
module "spark-glue" {
  source = "./modules/glue"

  glue_job_name         = var.glue_job_name
  glue_service_role_arn = var.glue_service_role_arn
  glue_version          = var.glue_version
}

# kinesis
module "kinesis" {
  source = "./modules/kinesis"

  kinesis_stream_name        = var.kinesis_stream_name
  kinesis_stream_shard_count = var.kinesis_stream_shard_count
  kinesis_firehose_name      = var.kinesis_firehose_name
  s3_bucket_arn              = module.s3.bucket_arn
  s3_bucket_prefix           = var.s3_bucket_prefix
  role_arn                   = var.role_arn
  kinesis_buffer_interval    = var.kinesis_buffer_interval
}


