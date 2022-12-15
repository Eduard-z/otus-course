import re
import os
import json

from jsonschema.validators import validate
from requests import Response, Session


def establish_session() -> Session:
    return Session()


def custom_request(base_url: str, endpoint: str, request_method: str, session: Session, **kwargs) -> Response:
    target = base_url + endpoint
    return session.request(method=request_method, url=target, **kwargs)


def check_status_code(response: Response, code: int):
    assert response.status_code == code, \
        f"Expected code {code} but got {response.status_code} instead"


def get_cart_id(response: Response) -> str:
    return response.json()["products"][0]["cart_id"]


def check_success_message(response: Response, message: str):
    assert response.json()["success"] == message, \
        f"Wrong message '{response.json().get('success')}'"


def check_error_message(response: Response, message: dict):
    assert response.json()["error"] == message, \
        f"Wrong message '{response.json().get('error')}'"


def check_product_id(response: Response, product_id: str):
    assert response.json()["products"][0]["product_id"] == product_id, \
        f"Expected product ID to equal '{product_id}' but it is '{response.json().get('products')[0]['product_id']}'"


def check_product_quantity(response: Response, quantity: str):
    assert response.json()["products"][0]["quantity"] == quantity, \
        f"Expected product Qty to equal '{quantity}' but it is '{response.json().get('products')[0]['quantity']}'"


def check_no_products_in_cart(response: Response):
    assert response.json()["products"] == [], \
        "Expected no products placed in the cart"


def check_response_empty(response: Response):
    assert response.json() == [], \
        "Response should be empty"


def check_response_text(response: Response, text: str):
    assert response.text == text, \
        f"Wrong message '{response.text}'"


def retrieve_quantity(incorrect_quantity: str) -> str:
    return re.match(r"(\d+)\D", incorrect_quantity.strip()).group(1)


def validate_json_schema(response: Response, json_file):
    absolute_path = os.path.dirname(__file__)
    relative_path = f"./schemas/{json_file}"
    full_path = os.path.join(absolute_path, relative_path)

    with open(os.path.expanduser(full_path)) \
            as response_schema:
        schema = json.load(response_schema)

        validate(instance=response.json(), schema=schema)
