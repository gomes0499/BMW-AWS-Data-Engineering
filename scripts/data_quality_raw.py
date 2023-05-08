import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsgluedq.transforms import EvaluateDataQuality

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init("glue-job-quality-raw")

# Script generated for node S3 bucket
S3bucket_node1 = glueContext.create_dynamic_frame.from_options(
    format_options={"multiline": False},
    connection_type="s3",
    format="json",
    connection_options={
        "paths": [
            "s3://wu10-datalake/raw/"
        ],
        "recurse": True,
    },
    transformation_ctx="S3bucket_node1",
)

# Script generated for node EvaluateDataQuality
EvaluateDataQuality_node2_ruleset = """
    Rules = [
        Completeness "vehicle_id" is 1,
        Completeness "timestamp" is 1,
        Completeness "sensor_data" is 1,
        Completeness "location" is 1,
        Distinctness "vehicle_id" is 1
    ]
"""

EvaluateDataQuality_node2_DQ_Results = EvaluateDataQuality.apply(
    frame=S3bucket_node1,
    ruleset=EvaluateDataQuality_node2_ruleset,
    publishing_options={
        "dataQualityEvaluationContext": "EvaluateDataQuality_node2",
        "enableDataQualityCloudWatchMetrics": True,
        "enableDataQualityResultsPublishing": True,
    },
)
EvaluateDataQuality_node2 = S3bucket_node1

job.commit()
