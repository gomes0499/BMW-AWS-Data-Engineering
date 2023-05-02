resource "aws_glue_job" "this" {
  name     = var.glue_job_name
  role_arn = var.glue_service_role_arn

  command {
    script_location = "${var.glue_scripts_bucket_arn}/${var.glue_script_name}"
    python_version  = "3"
    name            = "glueetl"
  }
}