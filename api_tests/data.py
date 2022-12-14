from types import SimpleNamespace
from faker import Faker

testvars = SimpleNamespace(
    SPECIAL="!@#$%^&*()_+=-~`[]\"{}|;\:',./?><",
    ALPHA_NUM="test1",
    TEXT_WITH_SPACES=" text with spaces ",
    SPACE=" ",
    EMPTY=""
)

routes = SimpleNamespace(
    ADD_TO_CART="/index.php?route=api/cart/add",
    EDIT_CART="/index.php?route=api/cart/edit",
    CART_PRODUCTS="/index.php?route=api/cart/products"
)

messages = SimpleNamespace(
    SUCCESS_MESSAGE="Success: You have modified your shopping cart!",
    PERMISSION_ERROR_WARNING={'warning': 'Warning: You do not have permission to access the API!'},
    PERMISSION_ERROR_MESSAGE="Warning: You do not have permission to access the API!",
    PRODUCT_ERROR_MESSAGE={'store': 'Product can not be bought from the store you have choosen!'},
    UNDEFINED_KEY_WARNING='<b>Warning</b>: Undefined array key "key" in '
                          '<b>/opt/bitnami/opencart/catalog/controller/api/cart.php</b> on line '
                          '<b>84</b>{"success":"Success: You have modified your shopping cart!"}',
    UNDEFINED_QUANTITY_WARNING='<b>Warning</b>: Undefined array key "quantity" in '
                               '<b>/opt/bitnami/opencart/catalog/controller/api/cart.php</b> on line '
                               '<b>84</b>{"success":"Success: You have modified your shopping cart!"}',
    UNDEFINED_KEY_QUANTITY_WARNING='<b>Warning</b>: Undefined array key "key" in '
                                   '<b>/opt/bitnami/opencart/catalog/controller/api/cart.php</b> on line <b>84</b>'
                                   '<b>Warning</b>: Undefined array key "quantity" in '
                                   '<b>/opt/bitnami/opencart/catalog/controller/api/cart.php</b> on line '
                                   '<b>84</b>{"success":"Success: You have modified your shopping cart!"}'
)


def fake_data() -> dict:
    fake = Faker()

    first_name = fake.first_name()
    last_name = fake.last_name()
    telephone = fake.phone_number()
    email_address = fake.email()
    password = fake.password()
    return {"first_name": first_name, "last_name": last_name, "email_address": email_address,
            "telephone": telephone, "password": password, "confirm_pass": password}
