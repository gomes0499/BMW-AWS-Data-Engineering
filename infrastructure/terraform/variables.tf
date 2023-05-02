# Variables for S3 Module
variable "bucket_name" {
  description = "The name of the S3 bucket to create"
  type        = string
}

variable "region" {
  description = "The AWS region where the s3 bucket will be created"
  type        = string
}

variable "glue_job_name" {
  description = "The name of the Glue job."
  type        = string
}

variable "glue_service_role_arn" {
  description = "The ARN of the IAM role with the necessary permissions for the Glue job."
  type        = string
}

variable "glue_script_name" {
  description = "The name of the Glue job script file."
  type        = string
}

