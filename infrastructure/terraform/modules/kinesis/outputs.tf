output "kinesis_stream_id" {
  description = "ID of the Kinesis Data Stream"
  value       = aws_kinesis_stream.this.id
}

output "kinesis_firehose_id" {
  description = "ID of the Kinesis Data Firehose"
  value       = aws_kinesis_firehose_delivery_stream.this.id
}



