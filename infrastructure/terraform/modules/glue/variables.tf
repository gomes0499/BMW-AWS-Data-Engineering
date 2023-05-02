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

variable "glue_scripts_bucket_arn" {
  description = "The ARN of the S3 bucket containing the Glue job script."
  type        = string
}