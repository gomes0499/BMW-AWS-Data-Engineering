import boto3
import configparser

config = configparser.ConfigParser()
config.read("../config/config.ini")


# Configure your AWS credentials and region
region_name = config.get("AWS", "region_name")

# Initialize the Athena client
client = boto3.client(
    "athena",
)

# Set the SQL query and the output location for the query results
sql_query = """
CREATE EXTERNAL TABLE IF NOT EXISTS `bmw_database`.`bmw_table` (
  `vehicle_id` string,
  `timestamp` timestamp,
  `sensor_data` struct<
    `engine_temperature`: struct<
      `front_left`: float,
      `front_right`: float,
      `rear_left`: float,
      `rear_right`: float
    >,
    `oil_pressure`: float,
    `battery_voltage`: float,
    `braked_pad_wear`: float,
    `transmission_temperature`: float,
    `fuel_level`: float,
    `odometer`: float
  >,
  `location` struct<
    `latitude`: float,
    `longitude`: float
  >
)
ROW FORMAT SERDE 'org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe'
STORED AS INPUTFORMAT 'org.apache.hadoop.hive.ql.io.parquet.MapredParquetInputFormat'
OUTPUTFORMAT 'org.apache.hadoop.hive.ql.io.parquet.MapredParquetOutputFormat'
LOCATION 's3://wu10-datalake/processed/'
TBLPROPERTIES ('classification' = 'parquet');
"""

output_location = "s3://wu10athena-queries"

# Execute the SQL query
response = client.start_query_execution(
    QueryString=sql_query,
    QueryExecutionContext={"Database": "bmw_database"},
    ResultConfiguration={"OutputLocation": output_location},
)

# Get the query execution ID
query_execution_id = response["QueryExecutionId"]
print(f"Query execution ID: {query_execution_id}")

# Check the query execution status
while True:
    query_status = client.get_query_execution(QueryExecutionId=query_execution_id)
    query_state = query_status["QueryExecution"]["Status"]["State"]
    if query_state in ("SUCCEEDED", "FAILED", "CANCELLED"):
        print(f"Query status: {query_state}")
        break
