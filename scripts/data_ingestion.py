import json
import random
import time
import boto3
import configparser
import os
from datetime import datetime

# Get the kinesis stream_name
config = configparser.ConfigParser()
config.read("../config/config.ini")
stream_name = config.get("KINESIS", "stream_name")

kinesis_client = boto3.client(
    "kinesis",
    # region_name=os.environ.get("AWS_REGION"),
    # aws_access_key_id=os.environ.get("AWS_ACCESS_KEY_ID"),
    # aws_secret_access_key=os.environ.get("AWS_SECRET_ACCESS_KEY"),
)


def generate_sensor_data():
    return {
        "engine_temperature": round(random.uniform(80, 110), 1),
        "oil_pressure": round(random.uniform(40, 50), 1),
        "battery_voltage": round(random.uniform(12, 14), 1),
        "braked_pad_wear": round(random.uniform(0, 100), 1),
        "tire_pressure": {
            "front_left": round(random.uniform(30, 35), 1),
            "front_right": round(random.uniform(30, 35), 1),
            "rear_left": round(random.uniform(30, 35), 1),
            "front_right": round(random.uniform(30, 35), 1),
        },
        "transmission_temperature": round(random.uniform(70, 95), 1),
        "fuel_level": round(random.uniform(0, 100), 1),
        "odometer": round(random.uniform(10000, 50000), 0),
    }


def generate_location():
    return {
        "latitude": round(random.uniform(37.7, 37.8), 4),
        "longitude": round(random.uniform(-122.5, -122.4), 4),
    }


def generate_bmw_data(vehicle_id):
    return {
        "vehicle_id": vehicle_id,
        "timestamp": datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"),
        "sensor_data": generate_sensor_data(),
        "location": generate_location(),
    }


def stream_bmw_data(vehicle_id, interval=1):
    for _ in range(300 // interval):
        bmw_data = generate_bmw_data(vehicle_id)
        print(json.dumps(bmw_data, indent=2))
        time.sleep(interval)


def send_data_to_kinesis(vehicle_id, interval=1):
    for _ in range(300 // interval):
        bmw_data = generate_bmw_data(vehicle_id)
        kinesis_record = {
            "Data": json.dumps(bmw_data) + "\n",
            "PartitionKey": vehicle_id,
        }
        response = kinesis_client.put_record(StreamName=stream_name, **kinesis_record)
        print(f"Sent data to Kinesis stream {stream_name}: {response}")
        time.sleep(interval)


if __name__ == "__main__":
    vehicle_id = "BMW123"
    interval = 1
    send_data_to_kinesis(vehicle_id, interval)
