import pytest
import requests


def pytest_addoption(parser):
    parser.addoption(
        "--url",
        default="https://ya.ru",
        help="This is request URL"
    )

    parser.addoption(
        "--status_code",
        default=200,
        help="response status code",
        type=int
    )

    parser.addoption(
        "--method",
        default="get",
        choices=["get", "post", "put", "patch", "delete"],
        help="method to execute"
    )


@pytest.fixture
def base_url_yandex(request):
    return request.config.getoption("--url")


@pytest.fixture
def response_code(request):
    return request.config.getoption("--status_code")


@pytest.fixture
def request_method(request):
    return getattr(requests, request.config.getoption("--method"))
