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

resource "aws_glue_job" "data_quality_raw" {
  name         = var.glue_job_name_quality_raw
  role_arn     = var.glue_service_role_arn
  glue_version = var.glue_version

  command {
    script_location = "s3://wu10glue-scripts/spark/data_quality_raw.py"
    python_version  = "3"
    name            = "glueetl"
  }
}

resource "aws_glue_job" "data_quality_processed" {
  name         = var.glue_job_name_quality_processed
  role_arn     = var.glue_service_role_arn
  glue_version = var.glue_version

  command {
    script_location = "s3://wu10glue-scripts/spark/data_quality_processed.py"
    python_version  = "3"
    name            = "glueetl"
  }
}