import logging

import pytest

from pygeotemporal.sensors import SensorsApi
from pygeotemporal.streams import StreamsApi
from pygeotemporal.datapoints import DatapointsApi

sensor_id = ""
stream_id = ""
datapoint_id = ""


def test_datapoints_count_by_sensor_get(caplog, host, username, password):
    caplog.setLevel(logging.DEBUG)
    client = DatapointsApi(host=host, username=username, password=password)
    response = client.datapoints_count_by_sensor_get(950)
    sensors = response.text
    logging.info("%s sensors found", sensors)
    assert response.status_code == 200


def test_create_datapoints(caplog, host, username, password):
    global sensor_id, stream_id, datapoint_id
    caplog.setLevel(logging.DEBUG)

    sensor_client = SensorsApi(host=host, username=username, password=password)
    stream_client = StreamsApi(host=host, username=username, password=password)
    datapoint_client = DatapointsApi(host=host, username=username, password=password)

    sensor_json = sensor_client.sensor_create_json("Datapoints Testing sensor2", 40.1149202, -88.2270582, 0, "", "ER")
    response = sensor_client.sensor_post(sensor_json)
    body = response.json()
    sensor_id = body['id']
    sensor = (sensor_client.sensor_get(sensor_id)).json()

    stream_json = stream_client.stream_create_json_from_sensor(sensor["sensor"])
    stream_body = stream_client.stream_post_json(stream_json)
    stream_id = stream_body['id']

    datapoint = {
        "sensor_id": sensor_id,
        "geometry": {
            "type": "Point",
            "coordinates": [40.1149202, -88.2270582, 0]
        },
        "start_time": "2019-01-02T00:00:00Z",
        "stream_id": stream_id,
        "sensor_name": "Sensor #1",
        "end_time": "2019-02-02T00:00:00Z",
        "type": "Feature",
        "properties": {
            "temperature": "50",
            "qaqc": "2"
        }
    }
    datapoint_response = datapoint_client.datapoint_post(datapoint)
    datapoint_body = datapoint_response.json()
    datapoint_id = datapoint_body['id']

    assert datapoint_response.status_code == 200 and datapoint_id


def test_delete_datapoints(caplog, host, username, password):
    global sensor_id, stream_id, datapoint_id
    caplog.setLevel(logging.DEBUG)

    sensor_client = SensorsApi(host=host, username=username, password=password)

    response = sensor_client.sensor_delete(sensor_id)

    assert response.status_code == 200


def test_post_bulk(host, username, password):
    datapoints_client = DatapointsApi(host=host, username=username, password=password)
    datapoints_list = [{'start_time': '1976-05-24T00:00:00Z', 'end_time': '1976-05-24T00:00:00Z', 'type': 'Feature',
                        'geometry': {'type': 'Point', 'coordinates': [-94.2747222, 36.5027778, 0]}, 'stream_id': 5088,
                        'sensor_id': 4921, 'sensor_name': 'USGS-07188820', 'properties': {'nitrate-as-n-mgl': '1.50'}},
                       {'start_time': '1976-06-21T00:00:00Z', 'end_time': '1976-06-21T00:00:00Z', 'type': 'Feature',
                        'geometry': {'type': 'Point', 'coordinates': [-94.2747222, 36.5027778, 0]}, 'stream_id': 5088,
                        'sensor_id': 4921, 'sensor_name': 'USGS-07188820', 'properties': {'nitrate-as-n-mgl': '0.70'}},
                       {'start_time': '1976-07-21T00:00:00Z', 'end_time': '1976-07-21T00:00:00Z', 'type': 'Feature',
                        'geometry': {'type': 'Point', 'coordinates': [-94.2747222, 36.5027778, 0]}, 'stream_id': 5088,
                        'sensor_id': 4921, 'sensor_name': 'USGS-07188820', 'properties': {'nitrate-as-n-mgl': '0.93'}},
                       {'start_time': '1976-08-18T00:00:00Z', 'end_time': '1976-08-18T00:00:00Z', 'type': 'Feature',
                        'geometry': {'type': 'Point', 'coordinates': [-94.2747222, 36.5027778, 0]}, 'stream_id': 5088,
                        'sensor_id': 4921, 'sensor_name': 'USGS-07188820', 'properties': {'nitrate-as-n-mgl': '0.98'}},
                       {'start_time': '1976-09-15T00:00:00Z', 'end_time': '1976-09-15T00:00:00Z', 'type': 'Feature',
                        'geometry': {'type': 'Point', 'coordinates': [-94.2747222, 36.5027778, 0]}, 'stream_id': 5088,
                        'sensor_id': 4921, 'sensor_name': 'USGS-07188820', 'properties': {'nitrate-as-n-mgl': '0.70'}},
                       {'start_time': '1976-10-19T00:00:00Z', 'end_time': '1976-10-19T00:00:00Z', 'type': 'Feature',
                        'geometry': {'type': 'Point', 'coordinates': [-94.2747222, 36.5027778, 0]}, 'stream_id': 5088,
                        'sensor_id': 4921, 'sensor_name': 'USGS-07188820', 'properties': {'nitrate-as-n-mgl': '1.50'}},
                       {'start_time': '1976-11-23T00:00:00Z', 'end_time': '1976-11-23T00:00:00Z', 'type': 'Feature',
                        'geometry': {'type': 'Point', 'coordinates': [-94.2747222, 36.5027778, 0]}, 'stream_id': 5088,
                        'sensor_id': 4921, 'sensor_name': 'USGS-07188820', 'properties': {'nitrate-as-n-mgl': '1.20'}},
                       {'start_time': '1976-12-27T00:00:00Z', 'end_time': '1976-12-27T00:00:00Z', 'type': 'Feature',
                        'geometry': {'type': 'Point', 'coordinates': [-94.2747222, 36.5027778, 0]}, 'stream_id': 5088,
                        'sensor_id': 4921, 'sensor_name': 'USGS-07188820', 'properties': {'nitrate-as-n-mgl': '1.50'}},
                       {'start_time': '1977-03-16T00:00:00Z', 'end_time': '1977-03-16T00:00:00Z', 'type': 'Feature',
                        'geometry': {'type': 'Point', 'coordinates': [-94.2747222, 36.5027778, 0]}, 'stream_id': 5088,
                        'sensor_id': 4921, 'sensor_name': 'USGS-07188820', 'properties': {'nitrate-as-n-mgl': '1.70'}},
                       {'start_time': '1977-04-19T00:00:00Z', 'end_time': '1977-04-19T00:00:00Z', 'type': 'Feature',
                        'geometry': {'type': 'Point', 'coordinates': [-94.2747222, 36.5027778, 0]}, 'stream_id': 5088,
                        'sensor_id': 4921, 'sensor_name': 'USGS-07188820', 'properties': {'nitrate-as-n-mgl': '1.40'}},
                       {'start_time': '1977-06-14T00:00:00Z', 'end_time': '1977-06-14T00:00:00Z', 'type': 'Feature',
                        'geometry': {'type': 'Point', 'coordinates': [-94.2747222, 36.5027778, 0]}, 'stream_id': 5088,
                        'sensor_id': 4921, 'sensor_name': 'USGS-07188820', 'properties': {'nitrate-as-n-mgl': '0.31'}},
                       {'start_time': '1977-07-19T00:00:00Z', 'end_time': '1977-07-19T00:00:00Z', 'type': 'Feature',
                        'geometry': {'type': 'Point', 'coordinates': [-94.2747222, 36.5027778, 0]}, 'stream_id': 5088,
                        'sensor_id': 4921, 'sensor_name': 'USGS-07188820', 'properties': {'nitrate-as-n-mgl': '0.21'}},
                       {'start_time': '1977-08-16T00:00:00Z', 'end_time': '1977-08-16T00:00:00Z', 'type': 'Feature',
                        'geometry': {'type': 'Point', 'coordinates': [-94.2747222, 36.5027778, 0]}, 'stream_id': 5088,
                        'sensor_id': 4921, 'sensor_name': 'USGS-07188820', 'properties': {'nitrate-as-n-mgl': '0.23'}},
                       {'start_time': '1977-09-20T00:00:00Z', 'end_time': '1977-09-20T00:00:00Z', 'type': 'Feature',
                        'geometry': {'type': 'Point', 'coordinates': [-94.2747222, 36.5027778, 0]}, 'stream_id': 5088,
                        'sensor_id': 4921, 'sensor_name': 'USGS-07188820', 'properties': {'nitrate-as-n-mgl': '0.85'}},
                       {'start_time': '1977-10-18T00:00:00Z', 'end_time': '1977-10-18T00:00:00Z', 'type': 'Feature',
                        'geometry': {'type': 'Point', 'coordinates': [-94.2747222, 36.5027778, 0]}, 'stream_id': 5088,
                        'sensor_id': 4921, 'sensor_name': 'USGS-07188820', 'properties': {'nitrate-as-n-mgl': '1.00'}},
                       {'start_time': '1977-10-18T00:00:00Z', 'end_time': '1977-10-18T00:00:00Z', 'type': 'Feature',
                        'geometry': {'type': 'Point', 'coordinates': [-94.2747222, 36.5027778, 0]}, 'stream_id': 5088,
                        'sensor_id': 4921, 'sensor_name': 'USGS-07188820',
                        'properties': {'nitrate-nitrite-inorganic-total-as-n-mgl': '1.00'}},
                       {'start_time': '1977-11-15T00:00:00Z', 'end_time': '1977-11-15T00:00:00Z', 'type': 'Feature',
                        'geometry': {'type': 'Point', 'coordinates': [-94.2747222, 36.5027778, 0]}, 'stream_id': 5088,
                        'sensor_id': 4921, 'sensor_name': 'USGS-07188820', 'properties': {'nitrate-as-n-mgl': '1.20'}},
                       {'start_time': '1977-11-15T00:00:00Z', 'end_time': '1977-11-15T00:00:00Z', 'type': 'Feature',
                        'geometry': {'type': 'Point', 'coordinates': [-94.2747222, 36.5027778, 0]}, 'stream_id': 5088,
                        'sensor_id': 4921, 'sensor_name': 'USGS-07188820',
                        'properties': {'nitrate-nitrite-inorganic-total-as-n-mgl': '1.20'}},
                       {'start_time': '1977-12-14T00:00:00Z', 'end_time': '1977-12-14T00:00:00Z', 'type': 'Feature',
                        'geometry': {'type': 'Point', 'coordinates': [-94.2747222, 36.5027778, 0]}, 'stream_id': 5088,
                        'sensor_id': 4921, 'sensor_name': 'USGS-07188820', 'properties': {'nitrate-as-n-mgl': '0.99'}},
                       {'start_time': '1977-12-14T00:00:00Z', 'end_time': '1977-12-14T00:00:00Z', 'type': 'Feature',
                        'geometry': {'type': 'Point', 'coordinates': [-94.2747222, 36.5027778, 0]}, 'stream_id': 5088,
                        'sensor_id': 4921, 'sensor_name': 'USGS-07188820',
                        'properties': {'nitrate-nitrite-inorganic-total-as-n-mgl': '1.00'}},
                       {'start_time': '1978-01-30T00:00:00Z', 'end_time': '1978-01-30T00:00:00Z', 'type': 'Feature',
                        'geometry': {'type': 'Point', 'coordinates': [-94.2747222, 36.5027778, 0]}, 'stream_id': 5088,
                        'sensor_id': 4921, 'sensor_name': 'USGS-07188820', 'properties': {'nitrate-as-n-mgl': '1.90'}},
                       {'start_time': '1978-01-30T00:00:00Z', 'end_time': '1978-01-30T00:00:00Z', 'type': 'Feature',
                        'geometry': {'type': 'Point', 'coordinates': [-94.2747222, 36.5027778, 0]}, 'stream_id': 5088,
                        'sensor_id': 4921, 'sensor_name': 'USGS-07188820',
                        'properties': {'nitrate-nitrite-inorganic-total-as-n-mgl': '1.90'}},
                       {'start_time': '1978-02-20T00:00:00Z', 'end_time': '1978-02-20T00:00:00Z', 'type': 'Feature',
                        'geometry': {'type': 'Point', 'coordinates': [-94.2747222, 36.5027778, 0]}, 'stream_id': 5088,
                        'sensor_id': 4921, 'sensor_name': 'USGS-07188820', 'properties': {'nitrate-as-n-mgl': '2.00'}},
                       {'start_time': '1978-02-20T00:00:00Z', 'end_time': '1978-02-20T00:00:00Z', 'type': 'Feature',
                        'geometry': {'type': 'Point', 'coordinates': [-94.2747222, 36.5027778, 0]}, 'stream_id': 5088,
                        'sensor_id': 4921, 'sensor_name': 'USGS-07188820',
                        'properties': {'nitrate-nitrite-inorganic-total-as-n-mgl': '2.00'}},
                       {'start_time': '1978-03-20T00:00:00Z', 'end_time': '1978-03-20T00:00:00Z', 'type': 'Feature',
                        'geometry': {'type': 'Point', 'coordinates': [-94.2747222, 36.5027778, 0]}, 'stream_id': 5088,
                        'sensor_id': 4921, 'sensor_name': 'USGS-07188820', 'properties': {'nitrate-as-n-mgl': '2.30'}},
                       {'start_time': '1978-03-20T00:00:00Z', 'end_time': '1978-03-20T00:00:00Z', 'type': 'Feature',
                        'geometry': {'type': 'Point', 'coordinates': [-94.2747222, 36.5027778, 0]}, 'stream_id': 5088,
                        'sensor_id': 4921, 'sensor_name': 'USGS-07188820',
                        'properties': {'nitrate-nitrite-inorganic-total-as-n-mgl': '2.30'}},
                       {'start_time': '1978-04-11T00:00:00Z', 'end_time': '1978-04-11T00:00:00Z', 'type': 'Feature',
                        'geometry': {'type': 'Point', 'coordinates': [-94.2747222, 36.5027778, 0]}, 'stream_id': 5088,
                        'sensor_id': 4921, 'sensor_name': 'USGS-07188820', 'properties': {'nitrate-as-n-mgl': '1.40'}},
                       {'start_time': '1978-04-11T00:00:00Z', 'end_time': '1978-04-11T00:00:00Z', 'type': 'Feature',
                        'geometry': {'type': 'Point', 'coordinates': [-94.2747222, 36.5027778, 0]}, 'stream_id': 5088,
                        'sensor_id': 4921, 'sensor_name': 'USGS-07188820',
                        'properties': {'nitrate-nitrite-inorganic-total-as-n-mgl': '1.40'}},
                       {'start_time': '1978-05-09T00:00:00Z', 'end_time': '1978-05-09T00:00:00Z', 'type': 'Feature',
                        'geometry': {'type': 'Point', 'coordinates': [-94.2747222, 36.5027778, 0]}, 'stream_id': 5088,
                        'sensor_id': 4921, 'sensor_name': 'USGS-07188820', 'properties': {'nitrate-as-n-mgl': '1.30'}},
                       {'start_time': '1978-05-09T00:00:00Z', 'end_time': '1978-05-09T00:00:00Z', 'type': 'Feature',
                        'geometry': {'type': 'Point', 'coordinates': [-94.2747222, 36.5027778, 0]}, 'stream_id': 5088,
                        'sensor_id': 4921, 'sensor_name': 'USGS-07188820',
                        'properties': {'nitrate-nitrite-inorganic-total-as-n-mgl': '1.30'}},
                       {'start_time': '1978-06-06T00:00:00Z', 'end_time': '1978-06-06T00:00:00Z', 'type': 'Feature',
                        'geometry': {'type': 'Point', 'coordinates': [-94.2747222, 36.5027778, 0]}, 'stream_id': 5088,
                        'sensor_id': 4921, 'sensor_name': 'USGS-07188820', 'properties': {'nitrate-as-n-mgl': '1.40'}},
                       {'start_time': '1978-06-06T00:00:00Z', 'end_time': '1978-06-06T00:00:00Z', 'type': 'Feature',
                        'geometry': {'type': 'Point', 'coordinates': [-94.2747222, 36.5027778, 0]}, 'stream_id': 5088,
                        'sensor_id': 4921, 'sensor_name': 'USGS-07188820',
                        'properties': {'nitrate-nitrite-inorganic-total-as-n-mgl': '1.40'}},
                       {'start_time': '1978-07-11T00:00:00Z', 'end_time': '1978-07-11T00:00:00Z', 'type': 'Feature',
                        'geometry': {'type': 'Point', 'coordinates': [-94.2747222, 36.5027778, 0]}, 'stream_id': 5088,
                        'sensor_id': 4921, 'sensor_name': 'USGS-07188820', 'properties': {'nitrate-as-n-mgl': '1.20'}},
                       {'start_time': '1978-07-11T00:00:00Z', 'end_time': '1978-07-11T00:00:00Z', 'type': 'Feature',
                        'geometry': {'type': 'Point', 'coordinates': [-94.2747222, 36.5027778, 0]}, 'stream_id': 5088,
                        'sensor_id': 4921, 'sensor_name': 'USGS-07188820',
                        'properties': {'nitrate-nitrite-inorganic-total-as-n-mgl': '1.20'}},
                       {'start_time': '1978-08-08T00:00:00Z', 'end_time': '1978-08-08T00:00:00Z', 'type': 'Feature',
                        'geometry': {'type': 'Point', 'coordinates': [-94.2747222, 36.5027778, 0]}, 'stream_id': 5088,
                        'sensor_id': 4921, 'sensor_name': 'USGS-07188820', 'properties': {'nitrate-as-n-mgl': '0.29'}},
                       {'start_time': '1978-08-08T00:00:00Z', 'end_time': '1978-08-08T00:00:00Z', 'type': 'Feature',
                        'geometry': {'type': 'Point', 'coordinates': [-94.2747222, 36.5027778, 0]}, 'stream_id': 5088,
                        'sensor_id': 4921, 'sensor_name': 'USGS-07188820',
                        'properties': {'nitrate-nitrite-inorganic-total-as-n-mgl': '0.300'}},
                       {'start_time': '1978-09-05T00:00:00Z', 'end_time': '1978-09-05T00:00:00Z', 'type': 'Feature',
                        'geometry': {'type': 'Point', 'coordinates': [-94.2747222, 36.5027778, 0]}, 'stream_id': 5088,
                        'sensor_id': 4921, 'sensor_name': 'USGS-07188820', 'properties': {'nitrate-as-n-mgl': '0.69'}},
                       {'start_time': '1978-09-05T00:00:00Z', 'end_time': '1978-09-05T00:00:00Z', 'type': 'Feature',
                        'geometry': {'type': 'Point', 'coordinates': [-94.2747222, 36.5027778, 0]}, 'stream_id': 5088,
                        'sensor_id': 4921, 'sensor_name': 'USGS-07188820',
                        'properties': {'nitrate-nitrite-inorganic-total-as-n-mgl': '0.700'}},
                       {'start_time': '1978-10-03T00:00:00Z', 'end_time': '1978-10-03T00:00:00Z', 'type': 'Feature',
                        'geometry': {'type': 'Point', 'coordinates': [-94.2747222, 36.5027778, 0]}, 'stream_id': 5088,
                        'sensor_id': 4921, 'sensor_name': 'USGS-07188820', 'properties': {'nitrate-as-n-mgl': '0.38'}},
                       {'start_time': '1978-10-31T00:00:00Z', 'end_time': '1978-10-31T00:00:00Z', 'type': 'Feature',
                        'geometry': {'type': 'Point', 'coordinates': [-94.2747222, 36.5027778, 0]}, 'stream_id': 5088,
                        'sensor_id': 4921, 'sensor_name': 'USGS-07188820', 'properties': {'nitrate-as-n-mgl': '0.96'}},
                       {'start_time': '1978-11-28T00:00:00Z', 'end_time': '1978-11-28T00:00:00Z', 'type': 'Feature',
                        'geometry': {'type': 'Point', 'coordinates': [-94.2747222, 36.5027778, 0]}, 'stream_id': 5088,
                        'sensor_id': 4921, 'sensor_name': 'USGS-07188820', 'properties': {'nitrate-as-n-mgl': '1.60'}},
                       {'start_time': '1979-01-09T00:00:00Z', 'end_time': '1979-01-09T00:00:00Z', 'type': 'Feature',
                        'geometry': {'type': 'Point', 'coordinates': [-94.2747222, 36.5027778, 0]}, 'stream_id': 5088,
                        'sensor_id': 4921, 'sensor_name': 'USGS-07188820', 'properties': {'nitrate-as-n-mgl': '2.00'}},
                       {'start_time': '1979-02-05T00:00:00Z', 'end_time': '1979-02-05T00:00:00Z', 'type': 'Feature',
                        'geometry': {'type': 'Point', 'coordinates': [-94.2747222, 36.5027778, 0]}, 'stream_id': 5088,
                        'sensor_id': 4921, 'sensor_name': 'USGS-07188820', 'properties': {'nitrate-as-n-mgl': '2.00'}},
                       {'start_time': '1979-03-05T00:00:00Z', 'end_time': '1979-03-05T00:00:00Z', 'type': 'Feature',
                        'geometry': {'type': 'Point', 'coordinates': [-94.2747222, 36.5027778, 0]}, 'stream_id': 5088,
                        'sensor_id': 4921, 'sensor_name': 'USGS-07188820', 'properties': {'nitrate-as-n-mgl': '2.10'}},
                       {'start_time': '1979-04-10T00:00:00Z', 'end_time': '1979-04-10T00:00:00Z', 'type': 'Feature',
                        'geometry': {'type': 'Point', 'coordinates': [-94.2747222, 36.5027778, 0]}, 'stream_id': 5088,
                        'sensor_id': 4921, 'sensor_name': 'USGS-07188820', 'properties': {'nitrate-as-n-mgl': '1.80'}},
                       {'start_time': '1979-05-08T00:00:00Z', 'end_time': '1979-05-08T00:00:00Z', 'type': 'Feature',
                        'geometry': {'type': 'Point', 'coordinates': [-94.2747222, 36.5027778, 0]}, 'stream_id': 5088,
                        'sensor_id': 4921, 'sensor_name': 'USGS-07188820', 'properties': {'nitrate-as-n-mgl': '1.50'}},
                       {'start_time': '1979-06-12T00:00:00Z', 'end_time': '1979-06-12T00:00:00Z', 'type': 'Feature',
                        'geometry': {'type': 'Point', 'coordinates': [-94.2747222, 36.5027778, 0]}, 'stream_id': 5088,
                        'sensor_id': 4921, 'sensor_name': 'USGS-07188820', 'properties': {'nitrate-as-n-mgl': '1.50'}},
                       {'start_time': '1979-07-17T00:00:00Z', 'end_time': '1979-07-17T00:00:00Z', 'type': 'Feature',
                        'geometry': {'type': 'Point', 'coordinates': [-94.2747222, 36.5027778, 0]}, 'stream_id': 5088,
                        'sensor_id': 4921, 'sensor_name': 'USGS-07188820', 'properties': {'nitrate-as-n-mgl': '0.90'}},
                       {'start_time': '1979-08-14T00:00:00Z', 'end_time': '1979-08-14T00:00:00Z', 'type': 'Feature',
                        'geometry': {'type': 'Point', 'coordinates': [-94.2747222, 36.5027778, 0]}, 'stream_id': 5088,
                        'sensor_id': 4921, 'sensor_name': 'USGS-07188820', 'properties': {'nitrate-as-n-mgl': '1.40'}},
                       {'start_time': '1979-09-10T00:00:00Z', 'end_time': '1979-09-10T00:00:00Z', 'type': 'Feature',
                        'geometry': {'type': 'Point', 'coordinates': [-94.2747222, 36.5027778, 0]}, 'stream_id': 5088,
                        'sensor_id': 4921, 'sensor_name': 'USGS-07188820', 'properties': {'nitrate-as-n-mgl': '0.59'}},
                       {'start_time': '1979-10-09T00:00:00Z', 'end_time': '1979-10-09T00:00:00Z', 'type': 'Feature',
                        'geometry': {'type': 'Point', 'coordinates': [-94.2747222, 36.5027778, 0]}, 'stream_id': 5088,
                        'sensor_id': 4921, 'sensor_name': 'USGS-07188820', 'properties': {'nitrate-as-n-mgl': '0.76'}},
                       {'start_time': '1979-12-04T00:00:00Z', 'end_time': '1979-12-04T00:00:00Z', 'type': 'Feature',
                        'geometry': {'type': 'Point', 'coordinates': [-94.2747222, 36.5027778, 0]}, 'stream_id': 5088,
                        'sensor_id': 4921, 'sensor_name': 'USGS-07188820', 'properties': {'nitrate-as-n-mgl': '1.80'}},
                       {'start_time': '1980-01-08T00:00:00Z', 'end_time': '1980-01-08T00:00:00Z', 'type': 'Feature',
                        'geometry': {'type': 'Point', 'coordinates': [-94.2747222, 36.5027778, 0]}, 'stream_id': 5088,
                        'sensor_id': 4921, 'sensor_name': 'USGS-07188820', 'properties': {'nitrate-as-n-mgl': '1.80'}},
                       {'start_time': '1980-02-05T00:00:00Z', 'end_time': '1980-02-05T00:00:00Z', 'type': 'Feature',
                        'geometry': {'type': 'Point', 'coordinates': [-94.2747222, 36.5027778, 0]}, 'stream_id': 5088,
                        'sensor_id': 4921, 'sensor_name': 'USGS-07188820', 'properties': {'nitrate-as-n-mgl': '2.80'}},
                       {'start_time': '1980-03-04T00:00:00Z', 'end_time': '1980-03-04T00:00:00Z', 'type': 'Feature',
                        'geometry': {'type': 'Point', 'coordinates': [-94.2747222, 36.5027778, 0]}, 'stream_id': 5088,
                        'sensor_id': 4921, 'sensor_name': 'USGS-07188820', 'properties': {'nitrate-as-n-mgl': '1.50'}},
                       {'start_time': '1980-04-01T00:00:00Z', 'end_time': '1980-04-01T00:00:00Z', 'type': 'Feature',
                        'geometry': {'type': 'Point', 'coordinates': [-94.2747222, 36.5027778, 0]}, 'stream_id': 5088,
                        'sensor_id': 4921, 'sensor_name': 'USGS-07188820', 'properties': {'nitrate-as-n-mgl': '1.70'}},
                       {'start_time': '1980-05-06T00:00:00Z', 'end_time': '1980-05-06T00:00:00Z', 'type': 'Feature',
                        'geometry': {'type': 'Point', 'coordinates': [-94.2747222, 36.5027778, 0]}, 'stream_id': 5088,
                        'sensor_id': 4921, 'sensor_name': 'USGS-07188820', 'properties': {'nitrate-as-n-mgl': '2.40'}},
                       {'start_time': '1980-06-03T00:00:00Z', 'end_time': '1980-06-03T00:00:00Z', 'type': 'Feature',
                        'geometry': {'type': 'Point', 'coordinates': [-94.2747222, 36.5027778, 0]}, 'stream_id': 5088,
                        'sensor_id': 4921, 'sensor_name': 'USGS-07188820', 'properties': {'nitrate-as-n-mgl': '0.93'}},
                       {'start_time': '1980-07-08T00:00:00Z', 'end_time': '1980-07-08T00:00:00Z', 'type': 'Feature',
                        'geometry': {'type': 'Point', 'coordinates': [-94.2747222, 36.5027778, 0]}, 'stream_id': 5088,
                        'sensor_id': 4921, 'sensor_name': 'USGS-07188820', 'properties': {'nitrate-as-n-mgl': '0.91'}},
                       {'start_time': '1980-07-29T00:00:00Z', 'end_time': '1980-07-29T00:00:00Z', 'type': 'Feature',
                        'geometry': {'type': 'Point', 'coordinates': [-94.2747222, 36.5027778, 0]}, 'stream_id': 5088,
                        'sensor_id': 4921, 'sensor_name': 'USGS-07188820', 'properties': {'nitrate-as-n-mgl': '0.24'}},
                       {'start_time': '1980-08-26T00:00:00Z', 'end_time': '1980-08-26T00:00:00Z', 'type': 'Feature',
                        'geometry': {'type': 'Point', 'coordinates': [-94.2747222, 36.5027778, 0]}, 'stream_id': 5088,
                        'sensor_id': 4921, 'sensor_name': 'USGS-07188820', 'properties': {'nitrate-as-n-mgl': '0.11'}},
                       {'start_time': '1980-09-23T00:00:00Z', 'end_time': '1980-09-23T00:00:00Z', 'type': 'Feature',
                        'geometry': {'type': 'Point', 'coordinates': [-94.2747222, 36.5027778, 0]}, 'stream_id': 5088,
                        'sensor_id': 4921, 'sensor_name': 'USGS-07188820', 'properties': {'nitrate-as-n-mgl': '0.05'}},
                       {'start_time': '1980-10-21T00:00:00Z', 'end_time': '1980-10-21T00:00:00Z', 'type': 'Feature',
                        'geometry': {'type': 'Point', 'coordinates': [-94.2747222, 36.5027778, 0]}, 'stream_id': 5088,
                        'sensor_id': 4921, 'sensor_name': 'USGS-07188820',
                        'properties': {'nitrate-nitrite-inorganic-total-as-n-mgl': '1.00'}},
                       {'start_time': '1981-02-17T00:00:00Z', 'end_time': '1981-02-17T00:00:00Z', 'type': 'Feature',
                        'geometry': {'type': 'Point', 'coordinates': [-94.2747222, 36.5027778, 0]}, 'stream_id': 5088,
                        'sensor_id': 4921, 'sensor_name': 'USGS-07188820',
                        'properties': {'nitrate-nitrite-inorganic-total-as-n-mgl': '1.70'}},
                       {'start_time': '1981-03-03T00:00:00Z', 'end_time': '1981-03-03T00:00:00Z', 'type': 'Feature',
                        'geometry': {'type': 'Point', 'coordinates': [-94.2747222, 36.5027778, 0]}, 'stream_id': 5088,
                        'sensor_id': 4921, 'sensor_name': 'USGS-07188820',
                        'properties': {'nitrate-nitrite-inorganic-total-as-n-mgl': '1.80'}},
                       {'start_time': '1981-03-17T00:00:00Z', 'end_time': '1981-03-17T00:00:00Z', 'type': 'Feature',
                        'geometry': {'type': 'Point', 'coordinates': [-94.2747222, 36.5027778, 0]}, 'stream_id': 5088,
                        'sensor_id': 4921, 'sensor_name': 'USGS-07188820',
                        'properties': {'nitrate-nitrite-inorganic-total-as-n-mgl': '1.80'}},
                       {'start_time': '1981-03-31T00:00:00Z', 'end_time': '1981-03-31T00:00:00Z', 'type': 'Feature',
                        'geometry': {'type': 'Point', 'coordinates': [-94.2747222, 36.5027778, 0]}, 'stream_id': 5088,
                        'sensor_id': 4921, 'sensor_name': 'USGS-07188820',
                        'properties': {'nitrate-nitrite-inorganic-total-as-n-mgl': '0.920'}},
                       {'start_time': '1981-05-05T00:00:00Z', 'end_time': '1981-05-05T00:00:00Z', 'type': 'Feature',
                        'geometry': {'type': 'Point', 'coordinates': [-94.2747222, 36.5027778, 0]}, 'stream_id': 5088,
                        'sensor_id': 4921, 'sensor_name': 'USGS-07188820',
                        'properties': {'nitrate-nitrite-inorganic-total-as-n-mgl': '0.970'}},
                       {'start_time': '1981-06-02T00:00:00Z', 'end_time': '1981-06-02T00:00:00Z', 'type': 'Feature',
                        'geometry': {'type': 'Point', 'coordinates': [-94.2747222, 36.5027778, 0]}, 'stream_id': 5088,
                        'sensor_id': 4921, 'sensor_name': 'USGS-07188820',
                        'properties': {'nitrate-nitrite-inorganic-total-as-n-mgl': '1.20'}},
                       {'start_time': '1981-06-30T00:00:00Z', 'end_time': '1981-06-30T00:00:00Z', 'type': 'Feature',
                        'geometry': {'type': 'Point', 'coordinates': [-94.2747222, 36.5027778, 0]}, 'stream_id': 5088,
                        'sensor_id': 4921, 'sensor_name': 'USGS-07188820',
                        'properties': {'nitrate-nitrite-inorganic-total-as-n-mgl': '0.590'}},
                       {'start_time': '1981-07-28T00:00:00Z', 'end_time': '1981-07-28T00:00:00Z', 'type': 'Feature',
                        'geometry': {'type': 'Point', 'coordinates': [-94.2747222, 36.5027778, 0]}, 'stream_id': 5088,
                        'sensor_id': 4921, 'sensor_name': 'USGS-07188820',
                        'properties': {'nitrate-nitrite-inorganic-total-as-n-mgl': '0.290'}},
                       {'start_time': '1981-08-11T00:00:00Z', 'end_time': '1981-08-11T00:00:00Z', 'type': 'Feature',
                        'geometry': {'type': 'Point', 'coordinates': [-94.2747222, 36.5027778, 0]}, 'stream_id': 5088,
                        'sensor_id': 4921, 'sensor_name': 'USGS-07188820',
                        'properties': {'nitrate-nitrite-inorganic-total-as-n-mgl': '0.640'}},
                       {'start_time': '1981-10-13T00:00:00Z', 'end_time': '1981-10-13T00:00:00Z', 'type': 'Feature',
                        'geometry': {'type': 'Point', 'coordinates': [-94.2747222, 36.5027778, 0]}, 'stream_id': 5088,
                        'sensor_id': 4921, 'sensor_name': 'USGS-07188820',
                        'properties': {'nitrate-nitrite-inorganic-total-as-n-mgl': '1.20'}},
                       {'start_time': '1981-12-08T00:00:00Z', 'end_time': '1981-12-08T00:00:00Z', 'type': 'Feature',
                        'geometry': {'type': 'Point', 'coordinates': [-94.2747222, 36.5027778, 0]}, 'stream_id': 5088,
                        'sensor_id': 4921, 'sensor_name': 'USGS-07188820',
                        'properties': {'nitrate-nitrite-inorganic-total-as-n-mgl': '1.80'}},
                       {'start_time': '1982-01-05T00:00:00Z', 'end_time': '1982-01-05T00:00:00Z', 'type': 'Feature',
                        'geometry': {'type': 'Point', 'coordinates': [-94.2747222, 36.5027778, 0]}, 'stream_id': 5088,
                        'sensor_id': 4921, 'sensor_name': 'USGS-07188820',
                        'properties': {'nitrate-nitrite-inorganic-total-as-n-mgl': '2.20'}},
                       {'start_time': '1982-02-09T00:00:00Z', 'end_time': '1982-02-09T00:00:00Z', 'type': 'Feature',
                        'geometry': {'type': 'Point', 'coordinates': [-94.2747222, 36.5027778, 0]}, 'stream_id': 5088,
                        'sensor_id': 4921, 'sensor_name': 'USGS-07188820',
                        'properties': {'nitrate-nitrite-inorganic-total-as-n-mgl': '2.30'}},
                       {'start_time': '1982-03-09T00:00:00Z', 'end_time': '1982-03-09T00:00:00Z', 'type': 'Feature',
                        'geometry': {'type': 'Point', 'coordinates': [-94.2747222, 36.5027778, 0]}, 'stream_id': 5088,
                        'sensor_id': 4921, 'sensor_name': 'USGS-07188820',
                        'properties': {'nitrate-nitrite-inorganic-total-as-n-mgl': '1.20'}},
                       {'start_time': '1982-05-04T00:00:00Z', 'end_time': '1982-05-04T00:00:00Z', 'type': 'Feature',
                        'geometry': {'type': 'Point', 'coordinates': [-94.2747222, 36.5027778, 0]}, 'stream_id': 5088,
                        'sensor_id': 4921, 'sensor_name': 'USGS-07188820',
                        'properties': {'nitrate-nitrite-inorganic-total-as-n-mgl': '1.40'}},
                       {'start_time': '1982-06-01T00:00:00Z', 'end_time': '1982-06-01T00:00:00Z', 'type': 'Feature',
                        'geometry': {'type': 'Point', 'coordinates': [-94.2747222, 36.5027778, 0]}, 'stream_id': 5088,
                        'sensor_id': 4921, 'sensor_name': 'USGS-07188820',
                        'properties': {'nitrate-nitrite-inorganic-total-as-n-mgl': '1.20'}},
                       {'start_time': '1982-07-06T00:00:00Z', 'end_time': '1982-07-06T00:00:00Z', 'type': 'Feature',
                        'geometry': {'type': 'Point', 'coordinates': [-94.2747222, 36.5027778, 0]}, 'stream_id': 5088,
                        'sensor_id': 4921, 'sensor_name': 'USGS-07188820',
                        'properties': {'nitrate-nitrite-inorganic-total-as-n-mgl': '0.690'}},
                       {'start_time': '1982-07-27T00:00:00Z', 'end_time': '1982-07-27T00:00:00Z', 'type': 'Feature',
                        'geometry': {'type': 'Point', 'coordinates': [-94.2747222, 36.5027778, 0]}, 'stream_id': 5088,
                        'sensor_id': 4921, 'sensor_name': 'USGS-07188820',
                        'properties': {'nitrate-nitrite-inorganic-total-as-n-mgl': '0.160'}},
                       {'start_time': '1982-08-17T00:00:00Z', 'end_time': '1982-08-17T00:00:00Z', 'type': 'Feature',
                        'geometry': {'type': 'Point', 'coordinates': [-94.2747222, 36.5027778, 0]}, 'stream_id': 5088,
                        'sensor_id': 4921, 'sensor_name': 'USGS-07188820',
                        'properties': {'nitrate-nitrite-inorganic-total-as-n-mgl': '0.490'}},
                       {'start_time': '1982-09-21T00:00:00Z', 'end_time': '1982-09-21T00:00:00Z', 'type': 'Feature',
                        'geometry': {'type': 'Point', 'coordinates': [-94.2747222, 36.5027778, 0]}, 'stream_id': 5088,
                        'sensor_id': 4921, 'sensor_name': 'USGS-07188820',
                        'properties': {'nitrate-nitrite-inorganic-total-as-n-mgl': '1.70'}},
                       {'start_time': '1982-10-19T00:00:00Z', 'end_time': '1982-10-19T00:00:00Z', 'type': 'Feature',
                        'geometry': {'type': 'Point', 'coordinates': [-94.2747222, 36.5027778, 0]}, 'stream_id': 5088,
                        'sensor_id': 4921, 'sensor_name': 'USGS-07188820',
                        'properties': {'nitrate-nitrite-inorganic-total-as-n-mgl': '0.240'}},
                       {'start_time': '1983-02-16T00:00:00Z', 'end_time': '1983-02-16T00:00:00Z', 'type': 'Feature',
                        'geometry': {'type': 'Point', 'coordinates': [-94.2747222, 36.5027778, 0]}, 'stream_id': 5088,
                        'sensor_id': 4921, 'sensor_name': 'USGS-07188820',
                        'properties': {'nitrate-nitrite-inorganic-total-as-n-mgl': '2.20'}},
                       {'start_time': '1983-03-08T00:00:00Z', 'end_time': '1983-03-08T00:00:00Z', 'type': 'Feature',
                        'geometry': {'type': 'Point', 'coordinates': [-94.2747222, 36.5027778, 0]}, 'stream_id': 5088,
                        'sensor_id': 4921, 'sensor_name': 'USGS-07188820',
                        'properties': {'nitrate-nitrite-inorganic-total-as-n-mgl': '1.16'}},
                       {'start_time': '1983-05-10T00:00:00Z', 'end_time': '1983-05-10T00:00:00Z', 'type': 'Feature',
                        'geometry': {'type': 'Point', 'coordinates': [-94.2747222, 36.5027778, 0]}, 'stream_id': 5088,
                        'sensor_id': 4921, 'sensor_name': 'USGS-07188820',
                        'properties': {'nitrate-nitrite-inorganic-total-as-n-mgl': '1.20'}},
                       {'start_time': '1983-06-28T00:00:00Z', 'end_time': '1983-06-28T00:00:00Z', 'type': 'Feature',
                        'geometry': {'type': 'Point', 'coordinates': [-94.2747222, 36.5027778, 0]}, 'stream_id': 5088,
                        'sensor_id': 4921, 'sensor_name': 'USGS-07188820',
                        'properties': {'nitrate-nitrite-inorganic-total-as-n-mgl': '1.50'}},
                       {'start_time': '1983-07-19T00:00:00Z', 'end_time': '1983-07-19T00:00:00Z', 'type': 'Feature',
                        'geometry': {'type': 'Point', 'coordinates': [-94.2747222, 36.5027778, 0]}, 'stream_id': 5088,
                        'sensor_id': 4921, 'sensor_name': 'USGS-07188820',
                        'properties': {'nitrate-nitrite-inorganic-total-as-n-mgl': '0.490'}},
                       {'start_time': '1983-08-16T00:00:00Z', 'end_time': '1983-08-16T00:00:00Z', 'type': 'Feature',
                        'geometry': {'type': 'Point', 'coordinates': [-94.2747222, 36.5027778, 0]}, 'stream_id': 5088,
                        'sensor_id': 4921, 'sensor_name': 'USGS-07188820',
                        'properties': {'nitrate-nitrite-inorganic-total-as-n-mgl': '0.260'}}]

    response = datapoints_client.datapoint_create_bulk(datapoints=datapoints_list)
    assert response.status_code == 200


@pytest.mark.skip(reason="This is a test for a specific sensor and stream, it should not be created every time a test "
                         "is ran")
def test_post_datapoint(host, username, password):
    datapoints_client = DatapointsApi(host=host, username=username, password=password)

    datapoint = {
        "sensor_id": "4879",
        "geometry": {
            "type": "Point",
            "coordinates": [-91.6221036, 40.0189337, 0]
        },
        "start_time": "2008-10-21T00:00:00Z",
        "stream_id": "5058",
        "sensor_name": "USGS-05497150",
        "end_time": "2008-10-21T00:00:00Z",
        "type": "Feature",
        "properties": {
            "nitrate-nitrite-inorganic-total-as-n-mgl": "0.21"
        }
    }
    response = datapoints_client.datapoint_post(datapoint)

    assert response.status_code == 200
