# Variables for S3 Module
variable "bucket_name" {
  description = "The name of the S3 bucket to create"
  type        = string
}

variable "region" {
  description = "The AWS region where the s3 bucket will be created"
  type        = string
}

# Variables for Glue Module
variable "glue_job_name" {
  description = "The name of the Glue job."
  type        = string
}

variable "glue_service_role_arn" {
  description = "The ARN of the IAM role with the necessary permissions for the Glue job."
  type        = string
}

variable "glue_version" {
  description = "The ARN of the S3 bucket containing the Glue job script."
  type        = string
}


# Variables for Kinesis Module
variable "kinesis_stream_name" {
  description = "Name of the Kinesis Data Stream"
  type        = string
}

variable "kinesis_stream_shard_count" {
  description = "Number of shards in the Kinesis Data Stream"
  type        = number
}

variable "kinesis_firehose_name" {
  description = "Name of the Kinesis Data Firehose"
  type        = string
}

variable "s3_bucket_prefix" {
  description = "Prefix for the S3 bucket used by the Kinesis Data Firehose"
  type        = string
}

variable "role_arn" {
  description = "Prefix for the S3 bucket used by the Kinesis Data Firehose"
  type        = string
}

variable "kinesis_buffer_interval" {
  description = "Number in seconds for kinesis buffer send data to s3"
  type        = number
}

