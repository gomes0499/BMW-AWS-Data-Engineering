variable "glue_job_name" {
  description = "The name of the Glue job."
  type        = string
}

variable "glue_service_role_arn" {
  description = "The ARN of the IAM role with the necessary permissions for the Glue job."
  type        = string
}

variable "glue_version" {
  description = "The glue spark version."
  type        = string
}

variable "glue_job_name_quality_raw" {
  description = "The name of the Glue job."
  type        = string
}

variable "glue_job_name_quality_processed" {
  description = "The name of the Glue job."
  type        = string
}