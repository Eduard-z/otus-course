import requests
import pytest
from .api_session import base_url, establish_session


@pytest.mark.parametrize("product_id, quantity", [('28', '1')])
def test_adding_product_to_cart(quantity, product_id):
    target = base_url + "/index.php?route=api/cart/add"
    api_token = establish_session().json()["api_token"]
    s = requests.Session()
    res_adding = s.post(url=target,
                        params={"api_token": api_token},
                        data={'product_id': product_id, 'quantity': quantity}
                        )
    assert res_adding.status_code == 200
    assert res_adding.json()["success"] == "Success: You have modified your shopping cart!"

    res_get = s.get(url=base_url + "/index.php?route=api/cart/products",
                    params={'api_token': api_token})
    assert res_get.status_code == 200
    assert res_get.json()["products"][0]["product_id"] == product_id
    assert res_get.json()["products"][0]["quantity"] == quantity
