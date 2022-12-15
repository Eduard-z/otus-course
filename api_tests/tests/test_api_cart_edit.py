import pytest
import allure
import api_tests.api as api
import api_tests.tests.test_api_cart_add as cart

from ..data import testvars, routes, messages


@allure.feature("[API] api/cart/edit")
@allure.story("[API] Edit products quantity in the cart")
@allure.title("[API] Edit product quantity")
@pytest.mark.parametrize("product_id, quantity, new_quantity",
                         [('28', '7', '13'), ('41', '12', '9'), ('41', '5', '5'), ('29', '4', '1234567890')],
                         ids=["increase", "decrease", "same", "big number"])
def test_edit_product_in_cart(base_url, session_token, quantity, product_id, new_quantity):
    with allure.step("Pre-condition: Add product to the cart"):
        cart.test_add_product_to_cart(base_url, session_token, quantity, product_id)

    with allure.step("Establish session with Opencart"):
        session = api.establish_session()

    with allure.step("Get cart id"):
        res_get = api.custom_request(request_method="GET",
                                     base_url=base_url, endpoint=routes.CART_PRODUCTS,
                                     session=session,
                                     params={'api_token': session_token}
                                     )
        cart_id = api.get_cart_id(res_get)

    with allure.step("Edit product quantity in the cart"):
        res_edit = api.custom_request(request_method="POST",
                                      base_url=base_url, endpoint=routes.EDIT_CART,
                                      session=session,
                                      params={"api_token": session_token},
                                      data={'key': cart_id, 'quantity': quantity}
                                      )
        api.check_status_code(res_edit, 200)
        api.check_success_message(res_edit, messages.SUCCESS_MESSAGE)

    with allure.step("Check your cart via API"):
        res_get = api.custom_request(request_method="GET",
                                     base_url=base_url, endpoint=routes.CART_PRODUCTS,
                                     session=session,
                                     params={'api_token': session_token}
                                     )
        api.check_status_code(res_get, 200)
        api.check_product_id(res_get, product_id)
        api.check_product_quantity(res_get, quantity)


@allure.feature("[API] api/cart/edit")
@allure.story("[API] Edit products quantity in the cart")
@allure.title("[API] Edit quantity: number with incorrect characters")
@pytest.mark.parametrize("product_id, quantity, new_quantity",
                         [('41', '12', '6.999'), ('41', '5', ' 33#'), ('29', '4', '7g')],
                         ids=["decimal", "spec chars", "letters"])
def test_edit_product_in_cart_incorrect_number(base_url, session_token, quantity, product_id, new_quantity):
    with allure.step("Pre-condition: Add product to the cart"):
        cart.test_add_product_to_cart(base_url, session_token, quantity, product_id)

    with allure.step("Establish session with Opencart"):
        session = api.establish_session()

    with allure.step("Get cart id"):
        res_get = api.custom_request(request_method="GET",
                                     base_url=base_url, endpoint=routes.CART_PRODUCTS,
                                     session=session,
                                     params={'api_token': session_token}
                                     )
        cart_id = api.get_cart_id(res_get)

    with allure.step("Edit product quantity in the cart"):
        res_edit = api.custom_request(request_method="POST",
                                      base_url=base_url, endpoint=routes.EDIT_CART,
                                      session=session,
                                      params={"api_token": session_token},
                                      data={'key': cart_id, 'quantity': new_quantity}
                                      )
        api.check_status_code(res_edit, 200)
        api.check_success_message(res_edit, messages.SUCCESS_MESSAGE)

    with allure.step("Check your cart via API: incorrect part is removed"):
        res_get = api.custom_request(request_method="GET",
                                     base_url=base_url, endpoint=routes.CART_PRODUCTS,
                                     session=session,
                                     params={'api_token': session_token}
                                     )
        api.check_status_code(res_get, 200)
        api.check_product_id(res_get, product_id)
        api.check_product_quantity(res_get, api.retrieve_quantity(new_quantity))


@allure.feature("[API] api/cart/edit")
@allure.story("[API] Edit products quantity in the cart")
@allure.title("[API] Edit quantity: no token parameter")
@pytest.mark.parametrize("product_id, quantity, new_quantity", [('29', '11', '12')], ids=["11 to 12"])
def test_edit_product_in_cart_no_token(base_url, session_token, quantity, product_id, new_quantity):
    with allure.step("Pre-condition: Add product to the cart"):
        cart.test_add_product_to_cart(base_url, session_token, quantity, product_id)

    with allure.step("Establish session with Opencart"):
        session = api.establish_session()

    with allure.step("Get cart id"):
        res_get = api.custom_request(request_method="GET",
                                     base_url=base_url, endpoint=routes.CART_PRODUCTS,
                                     session=session,
                                     params={'api_token': session_token}
                                     )
        cart_id = api.get_cart_id(res_get)

    with allure.step("Try to edit product quantity in the cart: without token"):
        res_edit = api.custom_request(request_method="POST",
                                      base_url=base_url, endpoint=routes.EDIT_CART,
                                      session=session,
                                      params={},
                                      data={'key': cart_id, 'quantity': new_quantity}
                                      )
        api.check_status_code(res_edit, 200)
        api.check_error_message(res_edit, messages.PERMISSION_ERROR_MESSAGE)

    with allure.step("Check your cart via API: quantity was not changed"):
        res_get = api.custom_request(request_method="GET",
                                     base_url=base_url, endpoint=routes.CART_PRODUCTS,
                                     session=session,
                                     params={'api_token': session_token}
                                     )
        api.check_status_code(res_get, 200)
        api.check_product_id(res_get, product_id)
        api.check_product_quantity(res_get, quantity)


@allure.feature("[API] api/cart/edit")
@allure.story("[API] Edit products quantity in the cart")
@allure.title("[API] Edit quantity: wrong token parameter")
@pytest.mark.parametrize("product_id, quantity, new_quantity", [('29', '8', '52')], ids=["8 to 52"])
@pytest.mark.parametrize("wrong_token", [testvars.ALPHA_NUM, testvars.TEXT_WITH_SPACES, 23, testvars.SPACE,
                                         testvars.EMPTY, testvars.SPECIAL, "8aaa410a2980bb7f90095f66b0"],
                         ids=["alpha_num", "text with spaces", "number", "space", "empty", "special", "old_token"])
def test_edit_product_in_cart_wrong_token(
        base_url, session_token, quantity, product_id, new_quantity, wrong_token
):
    with allure.step("Pre-condition: Add product to the cart"):
        cart.test_add_product_to_cart(base_url, session_token, quantity, product_id)

    with allure.step("Establish session with Opencart"):
        session = api.establish_session()

    with allure.step("Get cart id"):
        res_get = api.custom_request(request_method="GET",
                                     base_url=base_url, endpoint=routes.CART_PRODUCTS,
                                     session=session,
                                     params={'api_token': session_token}
                                     )
        cart_id = api.get_cart_id(res_get)

    with allure.step("Try to edit product quantity in the cart: wrong token"):
        res_edit = api.custom_request(request_method="POST",
                                      base_url=base_url, endpoint=routes.EDIT_CART,
                                      session=session,
                                      params={"api_token": wrong_token},
                                      data={'key': cart_id, 'quantity': new_quantity}
                                      )
        api.check_status_code(res_edit, 200)
        api.check_error_message(res_edit, messages.PERMISSION_ERROR_MESSAGE)

    with allure.step("Check your cart via API: quantity was not changed"):
        res_get = api.custom_request(request_method="GET",
                                     base_url=base_url, endpoint=routes.CART_PRODUCTS,
                                     session=session,
                                     params={'api_token': session_token}
                                     )
        api.check_status_code(res_get, 200)
        api.check_product_id(res_get, product_id)
        api.check_product_quantity(res_get, quantity)


@allure.feature("[API] api/cart/edit")
@allure.story("[API] Edit products quantity in the cart")
@allure.title("[API] Edit quantity: no cart ID parameter")
@pytest.mark.parametrize("product_id, quantity, new_quantity", [('29', '8', '52')], ids=["8 to 52"])
def test_edit_product_in_cart_no_cart_id(base_url, session_token, quantity, product_id, new_quantity):
    with allure.step("Pre-condition: Add product to the cart"):
        cart.test_add_product_to_cart(base_url, session_token, quantity, product_id)

    with allure.step("Establish session with Opencart"):
        session = api.establish_session()

    with allure.step("Try to edit product quantity in the cart: without cart ID"):
        res_edit = api.custom_request(request_method="POST",
                                      base_url=base_url, endpoint=routes.EDIT_CART,
                                      session=session,
                                      params={"api_token": session_token},
                                      data={'quantity': new_quantity}
                                      )
        api.check_status_code(res_edit, 200)
        api.check_response_text(res_edit, messages.UNDEFINED_KEY_WARNING)

    with allure.step("Check your cart via API: quantity was not changed"):
        res_get = api.custom_request(request_method="GET",
                                     base_url=base_url, endpoint=routes.CART_PRODUCTS,
                                     session=session,
                                     params={'api_token': session_token}
                                     )
        api.check_status_code(res_get, 200)
        api.check_product_id(res_get, product_id)
        api.check_product_quantity(res_get, quantity)


@allure.feature("[API] api/cart/edit")
@allure.story("[API] Edit products quantity in the cart")
@allure.title("[API] Edit quantity: no product Quantity parameter")
@pytest.mark.parametrize("product_id, quantity", [('29', '8')])
def test_edit_product_in_cart_no_quantity(base_url, session_token, quantity, product_id):
    with allure.step("Pre-condition: Add product to the cart"):
        cart.test_add_product_to_cart(base_url, session_token, quantity, product_id)

    with allure.step("Establish session with Opencart"):
        session = api.establish_session()

    with allure.step("Get cart id"):
        res_get = api.custom_request(request_method="GET",
                                     base_url=base_url, endpoint=routes.CART_PRODUCTS,
                                     session=session,
                                     params={'api_token': session_token}
                                     )
        cart_id = api.get_cart_id(res_get)

    with allure.step("Try to edit product quantity in the cart: without quantity"):
        res_edit = api.custom_request(request_method="POST",
                                      base_url=base_url, endpoint=routes.EDIT_CART,
                                      session=session,
                                      params={"api_token": session_token},
                                      data={'key': cart_id}
                                      )
        api.check_status_code(res_edit, 200)
        api.check_response_text(res_edit, messages.UNDEFINED_QUANTITY_WARNING)

    with allure.step("Check your cart via API: product is removed from the cart"):
        res_get = api.custom_request(request_method="GET",
                                     base_url=base_url, endpoint=routes.CART_PRODUCTS,
                                     session=session,
                                     params={'api_token': session_token}
                                     )
        api.check_status_code(res_get, 200)
        api.check_no_products_in_cart(res_get)


@allure.feature("[API] api/cart/edit")
@allure.story("[API] Edit products quantity in the cart")
@allure.title("[API] Edit quantity: no product Quantity and card ID parameters")
@pytest.mark.parametrize("product_id, quantity", [('29', '8')])
def test_edit_product_in_cart_no_quantity_card_id(base_url, session_token, quantity, product_id):
    with allure.step("Pre-condition: Add product to the cart"):
        cart.test_add_product_to_cart(base_url, session_token, quantity, product_id)

    with allure.step("Establish session with Opencart"):
        session = api.establish_session()

    with allure.step("Try to edit product quantity in the cart: without quantity and cart ID"):
        res_edit = api.custom_request(request_method="POST",
                                      base_url=base_url, endpoint=routes.EDIT_CART,
                                      session=session,
                                      params={"api_token": session_token},
                                      data={}
                                      )
        api.check_status_code(res_edit, 200)
        api.check_response_text(res_edit, messages.UNDEFINED_KEY_QUANTITY_WARNING)

    with allure.step("Check your cart via API: quantity was not changed"):
        res_get = api.custom_request(request_method="GET",
                                     base_url=base_url, endpoint=routes.CART_PRODUCTS,
                                     session=session,
                                     params={'api_token': session_token}
                                     )
        api.check_status_code(res_get, 200)
        api.check_product_id(res_get, product_id)
        api.check_product_quantity(res_get, quantity)


@allure.feature("[API] api/cart/edit")
@allure.story("[API] Edit products quantity in the cart")
@allure.title("[API] Edit quantity: wrong cart ID parameter")
@pytest.mark.parametrize("wrong_cart_id", ['-1', '0', '1.45', 'asd', 1234567890, testvars.SPECIAL,
                                           testvars.TEXT_WITH_SPACES, testvars.SPACE, testvars.EMPTY])
@pytest.mark.parametrize("product_id, quantity, new_quantity", [('29', '8', '52')], ids=["8 to 52"])
def test_edit_product_in_cart_wrong_cart_id(
        base_url, session_token, quantity, product_id, new_quantity, wrong_cart_id
):
    with allure.step("Pre-condition: Add product to the cart"):
        cart.test_add_product_to_cart(base_url, session_token, quantity, product_id)

    with allure.step("Establish session with Opencart"):
        session = api.establish_session()

    with allure.step("Try to edit product quantity in the cart: wrong cart ID"):
        res_edit = api.custom_request(request_method="POST",
                                      base_url=base_url, endpoint=routes.EDIT_CART,
                                      session=session,
                                      params={"api_token": session_token},
                                      data={'key': wrong_cart_id, 'quantity': new_quantity}
                                      )
        api.check_status_code(res_edit, 200)
        api.check_success_message(res_edit, messages.SUCCESS_MESSAGE)

    with allure.step("Check your cart via API: quantity was not changed"):
        res_get = api.custom_request(request_method="GET",
                                     base_url=base_url, endpoint=routes.CART_PRODUCTS,
                                     session=session,
                                     params={'api_token': session_token}
                                     )
        api.check_status_code(res_get, 200)
        api.check_product_id(res_get, product_id)
        api.check_product_quantity(res_get, quantity)


@allure.feature("[API] api/cart/edit")
@allure.story("[API] Edit products quantity in the cart")
@allure.title("[API] Edit quantity: wrong product Quantity parameter")
@pytest.mark.parametrize("wrong_new_quantity", ['-1', '0', 'asd', testvars.SPECIAL, testvars.ALPHA_NUM,
                                                testvars.TEXT_WITH_SPACES, testvars.SPACE, testvars.EMPTY])
@pytest.mark.parametrize("product_id, quantity", [('29', '8')])
def test_edit_product_in_cart_wrong_quantity(
        base_url, session_token, quantity, product_id, wrong_new_quantity
):
    with allure.step("Pre-condition: Add product to the cart"):
        cart.test_add_product_to_cart(base_url, session_token, quantity, product_id)

    with allure.step("Establish session with Opencart"):
        session = api.establish_session()

    with allure.step("Get cart id"):
        res_get = api.custom_request(request_method="GET",
                                     base_url=base_url, endpoint=routes.CART_PRODUCTS,
                                     session=session,
                                     params={'api_token': session_token}
                                     )
        cart_id = api.get_cart_id(res_get)

    with allure.step("Try to edit product quantity in the cart: wrong product Quantity"):
        res_edit = api.custom_request(request_method="POST",
                                      base_url=base_url, endpoint=routes.EDIT_CART,
                                      session=session,
                                      params={"api_token": session_token},
                                      data={'key': cart_id, 'quantity': wrong_new_quantity}
                                      )
        api.check_status_code(res_edit, 200)
        api.check_success_message(res_edit, messages.SUCCESS_MESSAGE)

    with allure.step("Check your cart via API: product is removed from the cart"):
        res_get = api.custom_request(request_method="GET",
                                     base_url=base_url, endpoint=routes.CART_PRODUCTS,
                                     session=session,
                                     params={'api_token': session_token}
                                     )
        api.check_status_code(res_get, 200)
        api.check_no_products_in_cart(res_get)
