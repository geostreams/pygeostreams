import logging

from pygeostreams.streams import StreamsApi
from pygeostreams.sensors import SensorsApi

sensor_id = ""
stream_id = ""


def test_streams_post(caplog, host, username, password):
    """
    This test attempts to create a stream given a sensor, and will fail
    if the stream that is trying to create already exists.

    """
    global sensor_id, stream_id
    caplog.setLevel(logging.DEBUG)

    sensor_client = SensorsApi(host=host, username=username, password=password)
    stream_client = StreamsApi(host=host, username=username, password=password)

    sensor_json = sensor_client.sensor_create_json("Testing sensor", 40.1149202, -88.2270582, 0, "", "ER")
    response = sensor_client.sensor_post(sensor_json)
    body = response.json()
    sensor_id = body['id']
    sensor = (sensor_client.sensor_get(sensor_id)).json()

    stream_json = stream_client.stream_create_json_from_sensor(sensor["sensor"])
    stream_body = stream_client.stream_post_json(stream_json)
    stream_id = stream_body['id']
    logging.info("Streams %i posted", stream_id)
    assert "id" in body

    # test get stream
    stream_response = stream_client.streams_get_by_id(stream_id)
    assert stream_response.status_code == 200 and stream_response.text is not None

    # test delete stream
    stream_response = stream_client.stream_delete(stream_id)
    stream_body = stream_response.json()

    logging.info("Sensor %s deleted", stream_id)
    assert stream_response.status_code == 200 and stream_body

    # delete sensor
    response = sensor_client.sensor_delete(sensor_id)
    sensor = response.json()
    logging.info("Sensor %s deleted" % sensor_id)
    assert response.status_code == 200 and sensor
