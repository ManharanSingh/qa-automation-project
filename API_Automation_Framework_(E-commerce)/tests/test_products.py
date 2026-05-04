import pytest
import os
import allure
from jsonschema import validate, FormatChecker
from utils.helpers import safe_json, load_test_data, assert_response_time
from data.schemas import product_schema

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DATA_FILE = os.path.join(BASE_DIR, "data", "test_data.json")

test_data = load_test_data(DATA_FILE)

@allure.feature("Product API")
@allure.story("Get product by ID")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.parametrize(
    "product_id, expected_valid",
    [(item['id'], item['expected_valid']) for item in test_data['products']],
    ids=[f"id={item['id']}" for item in test_data['products']]
)
def test_get_product_parametrized(product_service, product_id, expected_valid):
    allure.dynamic.title(f"Validate product API for ID: {product_id}")

    with allure.step("Send request"):
        response = product_service.get_product(product_id)

    with allure.step("Validate response"):
        assert response.status_code == 200
        assert_response_time(response)

    response_data = safe_json(response)

    if expected_valid:
        validate(instance=response_data, schema=product_schema, format_checker=FormatChecker())
        assert response_data["id"] == product_id
    else:
        assert response_data == {}, f"Expected empty response, got {response_data}"

def test_get_all_products(product_service):
    with allure.step("Send request"):
        response = product_service.get_all_products()

    assert response.status_code == 200
    assert_response_time(response)

    data = safe_json(response)

    assert isinstance(data, list)
    assert len(data) > 0

    for product in data:
        validate(instance=product, schema=product_schema, format_checker=FormatChecker())

def test_get_single_product(product_service):
    with allure.step("Send request"):
        response = product_service.get_product(1)

    assert response.status_code == 200
    assert_response_time(response)

    data = safe_json(response)

    validate(instance=data, schema=product_schema, format_checker=FormatChecker())
    assert data["id"] == 1
