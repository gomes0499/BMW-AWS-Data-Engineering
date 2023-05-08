variable "glue_job_name" {
  description = "The name of the Glue job."
  type        = string
}

variable "bucket_name" {
  description = "The name of the S3 bucket to create"
  type        = string
}

variable "kinesis_stream_name" {
  description = "Name of the Kinesis Data Stream"
  type        = string
}

variable "kinesis_firehose_name" {
  description = "Name of the Kinesis Data Firehose"
  type        = string
}