resource "aws_kinesis_stream" "this" {
  name        = var.kinesis_stream_name
  shard_count = var.kinesis_stream_shard_count
}

resource "aws_kinesis_firehose_delivery_stream" "this" {
  name        = var.kinesis_firehose_name
  destination = "s3"

  s3_configuration {
    role_arn        = var.role_arn
    bucket_arn      = var.s3_bucket_arn
    prefix          = var.s3_bucket_prefix
    buffer_interval = var.kinesis_buffer_interval
  }

  kinesis_source_configuration {
    kinesis_stream_arn = aws_kinesis_stream.this.arn
    role_arn           = var.role_arn
  }
}




