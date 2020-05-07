import pytest

from requests.exceptions import ConnectionError

from pygeotemporal.client import GeostreamsClient
from pygeotemporal.datapoints import DatapointsApi
from pygeotemporal.sensors import SensorsApi
from pygeotemporal.streams import StreamsApi


@pytest.fixture
def client(host, username, password):
    return GeostreamsClient(host=host, username=username, password=password)


@pytest.fixture
def sensors_client(host, username, password):
    return SensorsApi(host=host, username=username, password=password)


@pytest.fixture
def streams_client(host, username, password):
    return StreamsApi(host=host, username=username, password=password)


@pytest.fixture
def datapoints_client(host, username, password):
    return DatapointsApi(host=host, username=username, password=password)


def test_geostreams_client_connection_timeout(client):
    with pytest.raises(ConnectionError):
        client.get("/sensors", timeout=(0, 0))


def test_sensors_client_connection_timeout(sensors_client):
    with pytest.raises(ConnectionError):
        sensors_client.sensors_get(timeout=(0, 0))


def test_streams_client_connection_timeout(streams_client):
    with pytest.raises(ConnectionError):
        streams_client.streams_get(timeout=(0, 0))


def test_datapoints_client_connection_timeout(datapoints_client):
    with pytest.raises(ConnectionError):
        datapoints_client.datapoints_count_by_sensor_get(5750, timeout=(0, 0))


def test_client_wrong_timeout_tuple(client):
    with pytest.raises(ValueError):
        client.get("/sensors", timeout=(10, 10, 10, 10))


def test_sensors_client_wrong_timeout_tuple(sensors_client):
    with pytest.raises(ValueError):
        sensors_client.sensors_get(timeout=(10, 10, 10, 10))


def test_streams_client_wrong_timeout_tuple(streams_client):
    with pytest.raises(ValueError):
        streams_client.streams_get(timeout=(10, 10, 10, 10))


def test_datapoints_client_wrong_timeout_tuple(datapoints_client):
    with pytest.raises(ValueError):
        datapoints_client.datapoints_count_by_sensor_get(5750, timeout=(10, 10, 10, 10))
