import logging

import pytest
from requests import HTTPError

from pygeotemporal.client import GeostreamsClient
from pygeotemporal.sensors import SensorsApi


def test_get_sensors(caplog, host, username, password):
    caplog.setLevel(logging.DEBUG)
    client = SensorsApi(host=host, username=username, password=password)
    response = client.sensors_get()
    sensors = response.json()
    logging.info("%s sensors found", len(sensors))
    assert response.status_code == 200 and len(sensors) != 0


def test_raise_for_status(host, username, password):
    client = GeostreamsClient(host=host, username=username, password=password)
    with pytest.raises(HTTPError) as e:
        client.get_json("this_path_does_not_exist")
        assert e is not None
