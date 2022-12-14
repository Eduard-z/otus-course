import requests
import pytest
import os
from dotenv import load_dotenv

load_dotenv()


def pytest_addoption(parser):
    parser.addoption("--url", default="http://192.168.100.9:8081", help="Base Url for Opencart")


@pytest.fixture
def base_url(request):
    return request.config.getoption("--url")


@pytest.fixture()
def establish_session(base_url):
    target = base_url + "/index.php?route=api/login"
    s = requests.Session()
    response = s.post(url=target, data={'username': os.getenv("OPENCART_API_USERNAME"),
                                        'key': os.getenv("OPENCART_API_KEY")})
    return response


if __name__ == '__main__':
    res = establish_session()

    print("\n", res.status_code)
    print("\n", res.reason)
    print("\n", res.url)
    print("\n", res.headers)
    print("\n", res.json())
    print("\n", res.text)
    print("\n", res.cookies.keys())
    print("\n", res.request.headers)
    print("\n", res.request.body)
