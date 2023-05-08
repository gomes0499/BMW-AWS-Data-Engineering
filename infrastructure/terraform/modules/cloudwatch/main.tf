resource "aws_cloudwatch_metric_alarm" "kinesis_read_throughput_exceeded" {
  alarm_name          = "KinesisReadThroughputExceeded"
  comparison_operator = "GreaterThanOrEqualToThreshold"
  evaluation_periods  = "1"
  metric_name         = "ReadProvisionedThroughputExceeded"
  namespace           = "AWS/Kinesis"
  period              = "300"
  alarm_description   = "Alarm when read throughput exceeds the provisioned threshold."
  alarm_actions       = [aws_sns_topic.example.arn]
  threshold           = "1"
  ok_actions          = [aws_sns_topic.example.arn]
  dimensions = {
    StreamName = var.kinesis_stream_name
  }
  statistic = "SampleCount"
}

resource "aws_cloudwatch_metric_alarm" "kinesis_write_throughput_exceeded" {
  alarm_name          = "KinesisWriteThroughputExceeded"
  comparison_operator = "GreaterThanOrEqualToThreshold"
  evaluation_periods  = "1"
  metric_name         = "WriteProvisionedThroughputExceeded"
  namespace           = "AWS/Kinesis"
  period              = "300"
  alarm_description   = "Alarm when write throughput exceeds the provisioned threshold."
  alarm_actions       = [aws_sns_topic.example.arn]
  threshold           = "1"
  ok_actions          = [aws_sns_topic.example.arn]
  dimensions = {
    StreamName = var.kinesis_stream_name
  }
  statistic = "SampleCount"
}

resource "aws_cloudwatch_metric_alarm" "firehose_delivery_success" {
  alarm_name          = "FirehoseDeliverySuccess"
  comparison_operator = "LessThanThreshold"
  evaluation_periods  = "1"
  metric_name         = "DeliveryToS3.Success"
  namespace           = "AWS/Firehose"
  period              = "300"
  alarm_description   = "Alarm when the Firehose delivery success rate is below 90%."
  alarm_actions       = [aws_sns_topic.example.arn]
  threshold           = "90"
  ok_actions          = [aws_sns_topic.example.arn]
  dimensions = {
    DeliveryStreamName = var.kinesis_firehose_name
  }
  statistic = "Average"
}

resource "aws_cloudwatch_metric_alarm" "s3_number_of_objects" {
  alarm_name          = "S3NumberOfObjects"
  comparison_operator = "GreaterThanOrEqualToThreshold"
  evaluation_periods  = "1"
  metric_name         = "NumberOfObjects"
  namespace           = "AWS/S3"
  period              = "86400"
  alarm_description   = "Alarm when the number of objects in the S3 bucket exceeds a specified threshold."
  alarm_actions       = [aws_sns_topic.example.arn]
  threshold           = "1000000"
  ok_actions          = [aws_sns_topic.example.arn]
  dimensions = {
    BucketName  = var.bucket_name
    StorageType = "AllStorageTypes"
  }
  statistic = "Average"
}

resource "aws_cloudwatch_event_rule" "glue_job_run_failed" {
  name = "GlueJobRunFailed"
  event_pattern = jsonencode({
    "source" : ["aws.glue"],
    "detail-type" : ["Glue Job State Change"],
    "detail" : {
      "state" : ["FAILED"]
    }
  })
}

resource "aws_cloudwatch_event_target" "glue_job_run_failed_sns" {
  rule      = aws_cloudwatch_event_rule.glue_job_run_failed.name
  target_id = "SendNotification"
  arn       = aws_sns_topic.example.arn
}

resource "aws_sns_topic" "example" {
  name = "DataPipelineSNS"
}

resource "aws_sns_topic_subscription" "example_email" {
  topic_arn = aws_sns_topic.example.arn
  protocol  = "email"
  endpoint  = "notify.data.pipeline@gmail.com"
}


resource "aws_cloudwatch_dashboard" "example" {
  dashboard_name = "wu10DataPipelineDashboard"

  dashboard_body = jsonencode({
    widgets = [
      {
        type   = "metric"
        width  = 6
        height = 6
        properties = {
          metrics = [
            ["AWS/Kinesis", "ReadProvisionedThroughputExceeded", "StreamName", var.kinesis_stream_name],
            ["AWS/Kinesis", "WriteProvisionedThroughputExceeded", "StreamName", var.kinesis_stream_name],
            ["AWS/Kinesis", "GetRecords.IteratorAgeMilliseconds", "StreamName", var.kinesis_stream_name]
          ]
          view    = "timeSeries"
          stacked = false
          title   = "Kinesis Data Streams Metrics"
          region  = "us-east-1"
          period  = 300
        }
      },
      {
        type   = "metric"
        width  = 6
        height = 6
        properties = {
          metrics = [
            ["AWS/Firehose", "DeliveryToS3.DataFreshness", "DeliveryStreamName", var.kinesis_firehose_name],
            ["AWS/Firehose", "DeliveryToS3.RecordsDeliveryLatency", "DeliveryStreamName", var.kinesis_firehose_name],
            ["AWS/Firehose", "DeliveryToS3.Success", "DeliveryStreamName", var.kinesis_firehose_name]
          ]
          view    = "timeSeries"
          stacked = false
          title   = "Kinesis Data Firehose Metrics"
          region  = "us-east-1"
          period  = 300
        }
      },
      {
        type   = "metric"
        width  = 6
        height = 6
        properties = {
          metrics = [
            ["AWS/S3", "NumberOfObjects", "BucketName", var.bucket_name],
            ["AWS/S3", "BucketSizeBytes", "BucketName", var.bucket_name],
          ]
          view    = "timeSeries"
          stacked = false
          title   = "Amazon S3 Metrics"
          region  = "us-east-1"
          period  = 300
        }
      },
      {
        type   = "metric"
        width  = 6
        height = 6
        properties = {
          metrics = [
            ["AWS/Glue", "JobRunState", "JobName", var.glue_job_name],
            ["AWS/Glue", "BytesRead", "JobName", var.glue_job_name],
            ["AWS/Glue", "BytesWritten", "JobName", var.glue_job_name],
            ["AWS/Glue", "MillisBehindLatest", "JobName", var.glue_job_name]
          ]
          view    = "timeSeries"
          stacked = false
          title   = "AWS Glue Metrics"
          region  = "us-east-1"
          period  = 300
        }
      }
    ]
  })
}
