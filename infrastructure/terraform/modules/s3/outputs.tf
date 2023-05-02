output "bucket_id" {
  value       = aws_s3_bucket.datalake.id
  description = "The ID of the created S3 bucket."
}

output "raw_folder_key" {
  description = "The key of the raw folder in the S3 bucket."
  value       = aws_s3_object.raw_folder.id
}

output "processed_folder_key" {
  description = "The key of the processed folder in the S3 bucket."
  value       = aws_s3_object.processed_folder.id
}

output "bucket_arn" {
  description = "The ARN of the S3 bucket."
  value       = aws_s3_bucket.datalake.arn
}

output "glue_scripts_bucket_arn" {
  description = "The ARN of the S3 bucket containing the Glue job script."
  value       = aws_s3_bucket.glue_scripts.arn
}


output "airflow_scripts_bucket_arn" {
  description = "The ARN of the S3 bucket containing the Airflow script."
  value       = aws_s3_bucket.airflow_scripts.arn
}