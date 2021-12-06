import requests


def test_response_code(base_url_yandex, response_code):
    response = requests.get(url=base_url_yandex)
    assert response.status_code == int(response_code)
