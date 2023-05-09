import boto3
import os


def create_table_athena():
    # Initialize the Athena client
    client = boto3.client(
        "athena",
        region_name=os.environ.get("AWS_REGION"),
        aws_access_key_id=os.environ.get("AWS_ACCESS_KEY_ID"),
        aws_secret_access_key=os.environ.get("AWS_SECRET_ACCESS_KEY"),
    )

    # Set the SQL query and the output location for the query results
    sql_query = """
  CREATE EXTERNAL TABLE IF NOT EXISTS `bmw_database`.`bmw_table` (
    `vehicle_id` string,
    `timestamp` timestamp,
    `sensor_data` struct<
      `engine_temperature`: double,
      `tire_pressure`: struct<
        `front_left`: double,
        `front_right`: double,
        `rear_left`: double,
        `rear_right`: double
      >,
      `oil_pressure`: double,
      `battery_voltage`: double,
      `braked_pad_wear`: double,
      `transmission_temperature`: double,
      `fuel_level`: double,
      `odometer`: double
    >,
    `location` struct<
      `latitude`: double,
      `longitude`: double
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


create_table_athena()
