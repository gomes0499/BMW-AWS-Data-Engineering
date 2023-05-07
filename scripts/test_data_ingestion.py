import pytest
from data_ingestion import generate_sensor_data, generate_location, generate_bmw_data


def test_generate_sensor_data():
    sensor_data = generate_sensor_data()
    assert isinstance(sensor_data, dict)
    assert 80 <= sensor_data["engine_temperature"] <= 110
    assert 40 <= sensor_data["oil_pressure"] <= 50
    assert "tire_pressure" in sensor_data  
    tire_temp = sensor_data["tire_pressure"]
    for tire_position in ["front_left", "front_right", "rear_left", "front_right"]:
        assert 30 <= tire_temp[tire_position] <= 35



def test_generate_location():
    location = generate_location()
    assert isinstance(location, dict)
    assert "latitude" in location
    assert "longitude" in location
    assert 37.7 <= location["latitude"] <= 37.8
    assert -122.5 <= location["longitude"] <= -122.4


def test_generate_bmw_data():
    vehicle_id = "BMW123"
    bmw_data = generate_bmw_data(vehicle_id)
    assert isinstance(bmw_data, dict)
    assert "vehicle_id" in bmw_data
    assert "timestamp" in bmw_data
    assert "sensor_data" in bmw_data
    assert "location" in bmw_data
    assert bmw_data["vehicle_id"] == vehicle_id
    assert isinstance(bmw_data["sensor_data"], dict)
    assert isinstance(bmw_data["location"], dict)
