import requests
import pytest
from api_tests.dog_breeds_data import all_breeds_list, get_list_of_breeds_and_sub_breeds

base_url = "https://dog.ceo/api"


def test_get_single_random_image():
    target = base_url + "/breeds/image/random"
    response = requests.get(url=target)
    res_json = response.json()
    assert response.status_code == 200
    assert res_json.get("status") == "success"
    assert res_json.get("message").endswith(".jpg")


@pytest.mark.parametrize("images_number", [1, 12, 50], ids=["1 image", "12 images", "50 images"])
def test_get_multiple_random_images(images_number):
    target = base_url + f"/breeds/image/random/{images_number}"
    response = requests.get(url=target)
    res_json = response.json()
    assert response.status_code == 200
    assert res_json.get("status") == "success"
    assert len(res_json.get("message")) == images_number


@pytest.mark.parametrize("breed", all_breeds_list)
def test_get_array_of_images_from_a_breed(breed):
    target = base_url + f"/breed/{breed}/images"
    response = requests.get(url=target)
    res_json = response.json()
    assert response.status_code == 200
    assert res_json.get("status") == "success"
    for i in res_json.get("message"):
        assert breed in i


@pytest.mark.parametrize("breed", all_breeds_list)
def test_get_random_dog_image_from_a_breed(breed):
    target = base_url + f"/breed/{breed}/images/random"
    response = requests.get(url=target)
    res_json = response.json()
    assert response.status_code == 200
    assert res_json.get("status") == "success"
    assert breed in res_json.get("message")


@pytest.mark.parametrize("breed, sub_breed", get_list_of_breeds_and_sub_breeds())
def test_get_array_of_images_from_a_sub_breed(breed, sub_breed):
    target = base_url + "/breed/{}/{}/images".format(breed, sub_breed)
    response = requests.get(url=target)
    res_json = response.json()
    assert response.status_code == 200
    assert res_json.get("status") == "success"
    for i in res_json.get("message"):
        assert sub_breed in i


@pytest.mark.parametrize("breed, sub_breed", get_list_of_breeds_and_sub_breeds())
def test_get_random_dog_image_from_a_sub_breed(breed, sub_breed):
    target = base_url + "/breed/{}/{}/images/random".format(breed, sub_breed)
    response = requests.get(url=target)
    res_json = response.json()
    assert response.status_code == 200
    assert res_json.get("status") == "success"
    assert breed, sub_breed in res_json.get("message")
