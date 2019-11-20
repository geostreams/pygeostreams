import pytest


def pytest_addoption(parser):
    parser.addoption("--host", action="store", default="http://localhost:9000",
                     help="Host, including protocol and port. ")
    parser.addoption("--username", action="store",
                     help="Geostreams username")
    parser.addoption("--password", action="store",
                     help="Geostreams user password")


@pytest.fixture(scope="module")
def host(request):
    return request.config.getoption("--host")


@pytest.fixture(scope="module")
def username(request):
    return request.config.getoption("--username")


@pytest.fixture(scope="module")
def password(request):
    return request.config.getoption("--password")



