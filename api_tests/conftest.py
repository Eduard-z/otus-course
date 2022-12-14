import pytest
import os
import api_tests.api as api

from dotenv import load_dotenv

load_dotenv()


def pytest_addoption(parser):
    parser.addoption("--url", default="http://192.168.100.9:8081", help="Base Url for Opencart")


@pytest.fixture
def base_url(request):
    return request.config.getoption("--url")


@pytest.fixture
def session_token(base_url: str) -> str:
    session = api.establish_session()
    response = api.custom_request(request_method="POST",
                                  base_url=base_url, endpoint="/index.php?route=api/login",
                                  session=session,
                                  data={'username': os.getenv("OPENCART_API_USERNAME"),
                                        'key': os.getenv("OPENCART_API_KEY")}
                                  )
    return response.json()["api_token"]
