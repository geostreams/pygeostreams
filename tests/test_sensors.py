import logging

from pygeotemporal.sensors import SensorsApi

sensor_id = ""


def test_sensors_post(caplog, host, key):
    global sensor_id
    caplog.setLevel(logging.DEBUG)
    client = SensorsApi(host=host, key=key)
    sensor_json = client.sensor_create_json("Test Sensor", 40.1149202, -88.2270582, 0, "", "ER")
    response = client.sensor_post(sensor_json)
    body = response.json()
    sensor_id = body['id']
    logging.info("Sensor %i posted", body['id'])
    assert response.status_code == 200 and body

def test_sensors_get(caplog, host, key):
    global sensor_id
    caplog.setLevel(logging.DEBUG)
    client = SensorsApi(host=host, key=key)
    refresh = client.sensors_refresh_cache()
    assert refresh == True
    response = client.sensor_get(sensor_id)
    sensor = response.json()
    logging.info("Sensor %s found" % sensor_id)
    assert response.status_code == 200 and sensor

def test_sensors_delete(caplog, host, key):
    global sensor_id
    caplog.setLevel(logging.DEBUG)
    client = SensorsApi(host=host, key=key)
    response = client.sensor_delete(sensor_id)
    sensor = response.json()
    logging.info("Sensor %s deleted" % sensor_id)
    assert response.status_code == 200 and sensor
