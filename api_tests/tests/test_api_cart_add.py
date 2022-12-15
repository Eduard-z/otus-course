import pytest
import allure
import api_tests.api as api

from ..data import testvars, routes, messages


@allure.feature("[API] api/cart/add")
@allure.story("[API] Add products to the cart")
@allure.title("[API] Add product")
@pytest.mark.parametrize("product_id, quantity", [('28', '1'), ('28', '10'), ('29', '100'), ('29', '1234567890')],
                         ids=["one item", "10 items", "100 items", "big number"])
def test_add_product_to_cart(base_url, session_token, quantity, product_id):
    with allure.step("Establish session with Opencart"):
        session = api.establish_session()

    with allure.step("Add product to the cart"):
        res_add = api.custom_request(request_method="POST",
                                     base_url=base_url, endpoint=routes.ADD_TO_CART,
                                     session=session,
                                     params={"api_token": session_token},
                                     data={'product_id': product_id, 'quantity': quantity}
                                     )
        api.check_status_code(res_add, 200)
        api.check_success_message(res_add, messages.SUCCESS_MESSAGE)

    with allure.step("Check your cart via API"):
        res_get = api.custom_request(request_method="GET",
                                     base_url=base_url, endpoint=routes.CART_PRODUCTS,
                                     session=session,
                                     params={'api_token': session_token}
                                     )
        api.check_status_code(res_get, 200)
        api.check_product_id(res_get, product_id)
        api.check_product_quantity(res_get, quantity)


@allure.feature("[API] api/cart/add")
@allure.story("[API] Add products to the cart")
@allure.title("[API] Add product: number with incorrect characters")
@pytest.mark.parametrize("product_id, quantity", [('28', '6.999'), ('29', ' 33#'), ('29', '7g')],
                         ids=["decimal", "spec chars", "letters"])
def test_add_product_to_cart_incorrect_number(base_url, session_token, quantity, product_id):
    with allure.step("Establish session with Opencart"):
        session = api.establish_session()

    with allure.step("Add product to the cart"):
        res_add = api.custom_request(request_method="POST",
                                     base_url=base_url, endpoint=routes.ADD_TO_CART,
                                     session=session,
                                     params={"api_token": session_token},
                                     data={'product_id': product_id, 'quantity': quantity}
                                     )
        api.check_status_code(res_add, 200)
        api.check_success_message(res_add, messages.SUCCESS_MESSAGE)

    with allure.step("Check your cart via API: incorrect part is removed"):
        res_get = api.custom_request(request_method="GET",
                                     base_url=base_url, endpoint=routes.CART_PRODUCTS,
                                     session=session,
                                     params={'api_token': session_token}
                                     )
        api.check_status_code(res_get, 200)
        api.check_product_id(res_get, product_id)
        api.check_product_quantity(res_get, api.retrieve_quantity(quantity))


@allure.feature("[API] api/cart/add")
@allure.story("[API] Add products to the cart")
@allure.title("[API] Add product: no token parameter")
@pytest.mark.parametrize("product_id, quantity", [('29', '2')])
def test_add_product_to_cart_no_token(base_url, session_token, quantity, product_id):
    with allure.step("Establish session with Opencart"):
        session = api.establish_session()

    with allure.step("Try to add product to the cart: without token"):
        res_add = api.custom_request(request_method="POST",
                                     base_url=base_url, endpoint=routes.ADD_TO_CART,
                                     session=session,
                                     params={},
                                     data={'product_id': product_id, 'quantity': quantity}
                                     )
        api.check_status_code(res_add, 200)
        api.check_error_message(res_add, messages.PERMISSION_ERROR_WARNING)

    with allure.step("Check your cart via API: product was not added to the cart"):
        res_get = api.custom_request(request_method="GET",
                                     base_url=base_url, endpoint=routes.CART_PRODUCTS,
                                     session=session,
                                     params={'api_token': session_token}
                                     )
        api.check_status_code(res_get, 200)
        api.check_no_products_in_cart(res_get)


@allure.feature("[API] api/cart/add")
@allure.story("[API] Add products to the cart")
@allure.title("[API] Add product: wrong token parameter")
@pytest.mark.parametrize("product_id, quantity", [('29', '2')])
@pytest.mark.parametrize("wrong_token", [testvars.ALPHA_NUM, testvars.TEXT_WITH_SPACES, 23, testvars.SPACE,
                                         testvars.EMPTY, testvars.SPECIAL, "8aaa410a2980bb7f90095f66b0"],
                         ids=["alpha_num", "text with spaces", "number", "space", "empty", "special", "old_token"])
def test_add_product_to_cart_wrong_token(base_url, session_token, quantity, product_id, wrong_token):
    with allure.step("Establish session with Opencart"):
        session = api.establish_session()

    with allure.step("Try to add product to the cart: wrong token"):
        res_add = api.custom_request(request_method="POST",
                                     base_url=base_url, endpoint=routes.ADD_TO_CART,
                                     session=session,
                                     params={"api_token": wrong_token},
                                     data={'product_id': product_id, 'quantity': quantity}
                                     )
        api.check_status_code(res_add, 200)
        api.check_error_message(res_add, messages.PERMISSION_ERROR_WARNING)

    with allure.step("Check your cart via API: product was not added to the cart"):
        res_get = api.custom_request(request_method="GET",
                                     base_url=base_url, endpoint=routes.CART_PRODUCTS,
                                     session=session,
                                     params={'api_token': session_token}
                                     )
        api.check_status_code(res_get, 200)
        api.check_no_products_in_cart(res_get)


@allure.feature("[API] api/cart/add")
@allure.story("[API] Add products to the cart")
@allure.title("[API] Add product: no product ID parameter")
@pytest.mark.parametrize("quantity", ['17'])
def test_add_product_to_cart_no_product_id(base_url, session_token, quantity):
    with allure.step("Establish session with Opencart"):
        session = api.establish_session()

    with allure.step("Try to add product to the cart: without product ID"):
        res_add = api.custom_request(request_method="POST",
                                     base_url=base_url, endpoint=routes.ADD_TO_CART,
                                     session=session,
                                     params={"api_token": session_token},
                                     data={'quantity': quantity}
                                     )
        api.check_status_code(res_add, 200)
        api.check_response_empty(res_add)

    with allure.step("Check your cart via API: product was not added to the cart"):
        res_get = api.custom_request(request_method="GET",
                                     base_url=base_url, endpoint=routes.CART_PRODUCTS,
                                     session=session,
                                     params={'api_token': session_token}
                                     )
        api.check_status_code(res_get, 200)
        api.check_no_products_in_cart(res_get)


@allure.feature("[API] api/cart/add")
@allure.story("[API] Add products to the cart")
@allure.title("[API] Add product: no product Quantity parameter")
@pytest.mark.parametrize("product_id", ['29'])
def test_add_product_to_cart_no_quantity(base_url, session_token, product_id):
    with allure.step("Establish session with Opencart"):
        session = api.establish_session()

    with allure.step("Try to add product to the cart: without quantity"):
        res_add = api.custom_request(request_method="POST",
                                     base_url=base_url, endpoint=routes.ADD_TO_CART,
                                     session=session,
                                     params={"api_token": session_token},
                                     data={'product_id': product_id}
                                     )
        api.check_status_code(res_add, 200)
        api.check_success_message(res_add, messages.SUCCESS_MESSAGE)

    with allure.step("Check your cart via API: product quantity 1 was added to the cart"):
        res_get = api.custom_request(request_method="GET",
                                     base_url=base_url, endpoint=routes.CART_PRODUCTS,
                                     session=session,
                                     params={'api_token': session_token}
                                     )
        api.check_status_code(res_get, 200)
        api.check_product_id(res_get, product_id)
        api.check_product_quantity(res_get, quantity="1")


@allure.feature("[API] api/cart/add")
@allure.story("[API] Add products to the cart")
@allure.title("[API] Add product: no product ID and Quantity parameters")
def test_add_product_to_cart_no_product_id_quantity(base_url, session_token):
    with allure.step("Establish session with Opencart"):
        session = api.establish_session()

    with allure.step("Try to add product to the cart: without product ID and Quantity"):
        res_add = api.custom_request(request_method="POST",
                                     base_url=base_url, endpoint=routes.ADD_TO_CART,
                                     session=session,
                                     params={"api_token": session_token},
                                     data={}
                                     )
        api.check_status_code(res_add, 200)
        api.check_response_empty(res_add)

    with allure.step("Check your cart via API: product was not added to the cart"):
        res_get = api.custom_request(request_method="GET",
                                     base_url=base_url, endpoint=routes.CART_PRODUCTS,
                                     session=session,
                                     params={'api_token': session_token}
                                     )
        api.check_status_code(res_get, 200)
        api.check_no_products_in_cart(res_get)


@allure.feature("[API] api/cart/add")
@allure.story("[API] Add products to the cart")
@allure.title("[API] Add product: wrong product ID parameter")
@pytest.mark.parametrize("wrong_product_id", ['-1', '0', '1.45', 'asd', 1234567890, testvars.SPECIAL,
                                              testvars.TEXT_WITH_SPACES, testvars.SPACE, testvars.EMPTY])
@pytest.mark.parametrize("quantity", ['1'])
def test_add_product_to_cart_wrong_product_id(base_url, session_token, quantity, wrong_product_id):
    with allure.step("Establish session with Opencart"):
        session = api.establish_session()

    with allure.step("Try to add product to the cart: wrong product ID"):
        res_add = api.custom_request(request_method="POST",
                                     base_url=base_url, endpoint=routes.ADD_TO_CART,
                                     session=session,
                                     params={"api_token": session_token},
                                     data={'product_id': wrong_product_id, 'quantity': quantity}
                                     )
        api.check_status_code(res_add, 200)
        api.check_error_message(res_add, messages.PRODUCT_ERROR_MESSAGE)

    with allure.step("Check your cart via API: product was not added to the cart"):
        res_get = api.custom_request(request_method="GET",
                                     base_url=base_url, endpoint=routes.CART_PRODUCTS,
                                     session=session,
                                     params={'api_token': session_token}
                                     )
        api.check_status_code(res_get, 200)
        api.check_no_products_in_cart(res_get)


@allure.feature("[API] api/cart/add")
@allure.story("[API] Add products to the cart")
@allure.title("[API] Add product: wrong product Quantity parameter")
@pytest.mark.parametrize("wrong_quantity", ['-1', '0', 'asd', testvars.SPECIAL, testvars.ALPHA_NUM,
                                            testvars.TEXT_WITH_SPACES, testvars.SPACE, testvars.EMPTY])
@pytest.mark.parametrize("product_id", ['29'])
def test_add_product_to_cart_wrong_quantity(base_url, session_token, wrong_quantity, product_id):
    with allure.step("Establish session with Opencart"):
        session = api.establish_session()

    with allure.step("Try to add product to the cart: wrong product Quantity"):
        res_add = api.custom_request(request_method="POST",
                                     base_url=base_url, endpoint=routes.ADD_TO_CART,
                                     session=session,
                                     params={"api_token": session_token},
                                     data={'product_id': product_id, 'quantity': wrong_quantity}
                                     )
        api.check_status_code(res_add, 200)
        api.check_success_message(res_add, messages.SUCCESS_MESSAGE)

    with allure.step("Check your cart via API: product was not added to the cart"):
        res_get = api.custom_request(request_method="GET",
                                     base_url=base_url, endpoint=routes.CART_PRODUCTS,
                                     session=session,
                                     params={'api_token': session_token}
                                     )
        api.check_status_code(res_get, 200)
        api.check_no_products_in_cart(res_get)
