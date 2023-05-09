from awsglue.transforms import *
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsgluedq.transforms import EvaluateDataQuality


sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init("glue-spark-job")

# Script generated for node Data Lake Raw
DataLakeRaw_node1 = glueContext.create_dynamic_frame.from_options(
    format_options={"multiline": False},
    connection_type="s3",
    format="json",
    connection_options={"paths": ["s3://wu10-datalake/raw/"], "recurse": True},
    transformation_ctx="DataLakeRaw_node1",
)

# Script generated for node Raw Data Quality
RawDataQuality_node1683641470415_ruleset = """
    # You may insert rules from the DQDL rule builder to the left.
    # Choose "+" to insert rule types and column schema into the code editor.
    # Rules are inserted at cursor position.
    # e.g. Completeness "colA" between 0.4 and 0.8 */
    Rules = [
        ColumnExists "vehicle_id"
    ]
"""

RawDataQuality_node1683641470415_DQ_Results = EvaluateDataQuality.apply(
    frame=DataLakeRaw_node1,
    ruleset=RawDataQuality_node1683641470415_ruleset,
    publishing_options={
        "dataQualityEvaluationContext": "RawDataQuality_node1683641470415",
        "enableDataQualityCloudWatchMetrics": True,
        "enableDataQualityResultsPublishing": True,
    },
)
RawDataQuality_node1683641470415 = DataLakeRaw_node1

# Script generated for node Data Lake Processed
DataLakeProcessed_node3 = glueContext.write_dynamic_frame.from_options(
    frame=RawDataQuality_node1683641470415,
    connection_type="s3",
    format="glueparquet",
    connection_options={"path": "s3://wu10-datalake/processed/", "partitionKeys": []},
    format_options={"compression": "snappy"},
    transformation_ctx="DataLakeProcessed_node3",
)

job.commit()