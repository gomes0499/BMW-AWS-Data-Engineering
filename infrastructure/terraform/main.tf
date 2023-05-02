# S3
module "datalake_s3" {
  source = "./modules/S3"

  bucket_name = var.bucket_name
  region      = var.region
}

# Glue
module "spark-glue" {
  source = "./modules/glue"

  glue_job_name           = var.glue_job_name
  glue_service_role_arn   = var.glue_service_role_arn
  glue_script_name        = var.glue_script_name
  glue_scripts_bucket_arn = module.datalake_s3.glue_scripts_bucket_arn
}