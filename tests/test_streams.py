import logging

from pygeotemporal.streams import StreamsApi
from pygeotemporal.sensors import SensorsApi

sensor_id = ""
stream_id = ""


def test_streams_post(caplog, host, key):
    global sensor_id, stream_id
    caplog.setLevel(logging.DEBUG)
    sensor_client = SensorsApi(host=host, key=key)
    sensor_json = sensor_client.sensor_create_json("Test Sensor", 40.1149202, -88.2270582, 0, "", "ER")
    sensor_body = sensor_client.sensor_post_json(sensor_json)
    sensor_id = sensor_body['id']
    stream_client = StreamsApi(host=host, key=key)
    stream_json = stream_client.stream_create_json_from_sensor(sensor_body)
    body = stream_client.stream_post_json(stream_json)
    stream_id = body['id']
    logging.info("Streams %i posted", stream_id)
    assert "id" in body


def test_streams_get(caplog, host, key):
    global sensor_id, stream_id
    caplog.setLevel(logging.DEBUG)
    stream_client = StreamsApi(host=host, key=key)
    stream = stream_client.stream_get_by_name_json("Test Sensor")
    logging.info("Stream %s found", stream_id)
    assert stream


def test_streams_delete(caplog, host, key):
    global sensor_id, stream_id
    caplog.setLevel(logging.DEBUG)
    sensor_client = SensorsApi(host=host, key=key)
    response = sensor_client.sensor_delete(sensor_id)

    stream_client = StreamsApi(host=host, key=key)
    response = stream_client.stream_delete(stream_id)

    stream = response.json()
    logging.info("Sensor %s deleted", stream_id)
    assert response.status_code == 200 and stream
