import pytest


def pytest_addoption(parser):
    """
    自定义参数
    """
    parser.addoption("--cmdopt", action="store",default="device",help="None")


@pytest.fixture(scope="session")
def cmdopt(request):
    return request.config.getoption("--cmdopt")
