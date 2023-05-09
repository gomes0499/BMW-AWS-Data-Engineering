resource "aws_glue_job" "this" {
  name         = var.glue_job_name
  role_arn     = var.glue_service_role_arn
  glue_version = var.glue_version

  command {
    script_location = "s3://wu10glue-scripts/spark/spark-job.py"
    python_version  = "3"
    name            = "glueetl"
  }
}


