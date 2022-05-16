import requests
import pytest
from .api_session import base_url, establish_session
from .maria_db_config import cursor, db_connection


@pytest.mark.parametrize("product_id, quantity", [('28', '1')], ids=["one item"])
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

    # check your cart via API
    res_get = s.get(url=base_url + "/index.php?route=api/cart/products",
                    params={'api_token': api_token})
    assert res_get.status_code == 200
    assert res_get.json()["products"][0]["product_id"] == product_id
    assert res_get.json()["products"][0]["quantity"] == quantity

    # check your cart via SQL query
    sql_query = "SELECT product_id, quantity  FROM oc_cart WHERE session_id = ?"
    with db_connection:
        cursor.execute(sql_query, (api_token,))
        assert cursor.fetchall()[0] == (int(product_id), int(quantity))
