import pytest


def pytest_addoption(parser):
    parser.addoption("--host", action="store", default="default name")


@pytest.fixture(scope='session')
def host(request):
    host_value = request.config.option.host
    if host_value is None:
        pytest.skip()
    return host_value
