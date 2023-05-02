# Configure the backend to store state in S3
terraform {
  backend "s3" {
    bucket = "gomes-tf-state"
    key    = "project-tfstate"
    region = "us-east-1"
  }
}
