import logging

from pygeostreams.sensors import SensorsApi
import pytest
import json


# testing post, get, and delete here so we don't populate db with test sensors
def test_sensor_endpoint( host, username, password):
    client = SensorsApi(host=host, username=username, password=password)

    # test create sensor
    sensor_json = client.sensor_create_json("Test Sensor", 40.1149202, -88.2270582, 0, "", "ER")
    response = client.sensor_post(sensor_json)
    body = response.json()
    sensor_id = body['id']
    logging.info("Sensor %i posted", body['id'])
    assert response.status_code == 200 and body

    # test get sensor
    response = client.sensor_get(sensor_id)
    sensor = response.json()
    logging.info("Sensor %s found" % sensor_id)
    assert response.status_code == 200 and sensor

    # test update sensor
    response = client.sensor_statistics_post(int(sensor_id))
    assert response.status_code == 200

    # test delete sensor
    response = client.sensor_delete(sensor_id)
    sensor = response.json()
    logging.info("Sensor %s deleted" % sensor_id)
    assert response.status_code == 200 and sensor


@pytest.mark.skip(reason="need to manually set the sensor id")
def test_delete_sensor( host, username, password):
    client = SensorsApi(host=host, username=username, password=password)

    sensor_name = "USGS-07029150"

    r = client.sensor_get_by_name(sensor_name)
    sensor_r = json.loads(r.text)
    sensor_id = sensor_r["sensors"][0]["id"]
    response = client.sensor_delete(sensor_id)

    logging.info("Sensor %s deleted" % sensor_id)
    assert response.status_code == 200 and sensor_r
