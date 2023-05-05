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

variable "s3_bucket_arn" {
  description = "ARN of the S3 bucket for the Kinesis Data Firehose"
  type        = string
}

variable "s3_bucket_prefix" {
  description = "Prefix for the S3 bucket used by the Kinesis Data Firehose"
  type        = string
}

variable "kinesis_buffer_interval" {
  description = "Number in seconds for kinesis buffer send data to s3"
  type        = number
}


variable "role_arn" {
  description = "Prefix for the S3 bucket used by the Kinesis Data Firehose"
  type        = string
}

