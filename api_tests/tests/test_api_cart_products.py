import pytest
import allure
import api_tests.api as api
import api_tests.tests.test_api_cart_add as cart

from ..data import routes


@allure.feature("[API] api/cart/products")
@allure.story("[API] Get cart contents")
@allure.title("[API] Get cart contents")
@pytest.mark.parametrize("product_id, quantity", [('28', '1')])
def test_get_cart_products(base_url, session_token, quantity, product_id):
    with allure.step("Pre-condition: Add product to the cart"):
        cart.test_add_product_to_cart(base_url, session_token, quantity, product_id)

    with allure.step("Establish session with Opencart"):
        session = api.establish_session()

    with allure.step("Check your cart via API"):
        res_get = api.custom_request(request_method="GET",
                                     base_url=base_url, endpoint=routes.CART_PRODUCTS,
                                     session=session,
                                     params={'api_token': session_token}
                                     )
        api.check_status_code(res_get, 200)
        api.check_product_id(res_get, product_id)

    with allure.step("Check response schema"):
        api.validate_json_schema(res_get, "jsonschema_cart_products.json")
