import logging

from pygeotemporal.datapoints import DatapointsApi


def test_datapoints_count_by_sensor_get(caplog, host, key):
    caplog.setLevel(logging.DEBUG)
    client = DatapointsApi(host=host, key=key)
    response = client.datapoints_count_by_sensor_get(950)
    sensors = response.text
    logging.info("%s sensors found", sensors)
    assert response.status_code == 200
