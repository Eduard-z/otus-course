import requests
import pytest

base_url = "https://httpbin.org"


def test_get():
    target = base_url + "/get"
    response = requests.get(url=target)
    assert response.status_code == 200
    assert response.reason == "OK"
    assert response.url == "https://httpbin.org/get"
    assert response.headers['Content-Type'] == 'application/json'
    assert response.json()['headers']['Host'] == 'httpbin.org'
    assert response.cookies.keys() == []


def test_post():
    target = base_url + "/post"
    response = requests.post(url=target)
    assert response.status_code == 200
    assert response.reason == "OK"
    assert response.url == "https://httpbin.org/post"
    assert response.headers['Content-Type'] == 'application/json'
    assert response.json()['headers']['Host'] == 'httpbin.org'
    assert response.cookies.keys() == []


@pytest.mark.parametrize("code", [200, 300, 400, 500])
def test_post_status_codes(code):
    target = base_url + f"/status/{code}"
    response = requests.request(url=target, method="POST")
    assert response.status_code == code


@pytest.mark.parametrize("code", [200, 300, 400, 500])
def test_delete_status_codes(code):
    target = base_url + f"/status/{code}"
    response = requests.delete(url=target)
    assert response.status_code == code


@pytest.mark.parametrize("code", [200, 300, 400, 500])
def test_request_method_fixture_status_codes(code, request_method):
    target = base_url + f"/status/{code}"
    response = request_method(url=target)
    assert response.status_code == code


@pytest.mark.parametrize("code", [200, 300, 400, 500])
@pytest.mark.parametrize("req_method", ["POST", "GET", "PUT", "PATCH", "DELETE"])
def test_request_method_param_status_codes(code, req_method):
    target = base_url + f"/status/{code}"
    response = requests.request(url=target, method=req_method)
    assert response.status_code == code


@pytest.mark.parametrize("username, password", [('user1', 'password1'), ('user2', 'password2')])
def test_auth(username, password):
    target = base_url + f"/basic-auth/{username}/{password}"
    response = requests.get(url=target, auth=('user1', 'password1'))
    assert response.status_code >= 200
    print("\n", response.status_code)
    print("\n", response.reason)
    print("\n", response.url)
    print("\n", response.headers)
    #print("\n", response.json())
    print("\n", response.text)
    print("\n", response.cookies.keys())
    print("\n", response.request.headers)
    print("\n", response.request.body)
