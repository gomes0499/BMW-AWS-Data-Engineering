from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql.types import (
    StructType,
    StructField,
    StringType,
    TimestampType,
    DoubleType,
    MapType,
)

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init("glue-spark-job")

# Set the source and destination paths
source_bucket = "s3://wu10-datalake/raw/"
destination_bucket = "s3://wu10-datalake/processed/"

# Define the schema of the JSON data
schema = StructType(
    [
        StructField("vehicle_id", StringType(), True),
        StructField("timestamp", TimestampType(), True),
        StructField(
            "sensor_data",
            StructType(
                [
                    StructField("engine_temperature", DoubleType(), True),
                    StructField("oil_pressure", DoubleType(), True),
                    StructField("battery_voltage", DoubleType(), True),
                    StructField("brake_pad_wear", DoubleType(), True),
                    StructField(
                        "tire_pressure",
                        StructType(
                            [
                                StructField("front_left", DoubleType(), True),
                                StructField("front_right", DoubleType(), True),
                                StructField("rear_left", DoubleType(), True),
                                StructField("rear_right", DoubleType(), True),
                            ]
                        ),
                        True,
                    ),
                    StructField("transmission_temperature", DoubleType(), True),
                    StructField("fuel_level", DoubleType(), True),
                    StructField("odometer", DoubleType(), True),
                ]
            ),
            True,
        ),
        StructField(
            "location",
            StructType(
                [
                    StructField("latitude", DoubleType(), True),
                    StructField("longitude", DoubleType(), True),
                ]
            ),
            True,
        ),
    ]
)

# Read JSON data from S3 source using the defined schema
json_data = spark.read.format("json").schema(schema).load(source_bucket)

# Convert the data to Parquet format and write to the destination
json_data.write.format("parquet").mode("overwrite").save(destination_bucket)


job.commit()
