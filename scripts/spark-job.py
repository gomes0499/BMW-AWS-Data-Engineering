from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql.types import (
    StructType,
    StructField,
    StringType,
    TimestampType,
    FloatType,
)

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init("glue-spark-job")

# Set the source and destination paths
source_bucket = "s3://wu10-datalake/raw/*/*/*/*/"
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
                    StructField("engine_temperature", FloatType(), True),
                    StructField(
                        "tire_pressure",
                        StructType(
                            [
                                StructField("front_left", FloatType(), True),
                                StructField("front_right", FloatType(), True),
                                StructField("rear_left", FloatType(), True),
                                StructField("rear_right", FloatType(), True),
                            ]
                        ),
                        True,
                    ),
                    StructField("oil_pressure", FloatType(), True),
                    StructField("battery_voltage", FloatType(), True),
                    StructField("braked_pad_wear", FloatType(), True),
                    StructField("transmission_temperature", FloatType(), True),
                    StructField("fuel_level", FloatType(), True),
                    StructField("odometer", FloatType(), True),
                ]
            ),
            True,
        ),
        StructField(
            "location",
            StructType(
                [
                    StructField("latitude", FloatType(), True),
                    StructField("longitude", FloatType(), True),
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
