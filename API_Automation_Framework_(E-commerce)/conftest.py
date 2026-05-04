import pytest
from utils.api_client import APIClient
from services.product_service import ProductService

BASE_URL = "https://fakestoreapi.com"

@pytest.fixture(scope="session")
def api_client():
    return APIClient(base_url=BASE_URL)

@pytest.fixture
def product_service(api_client):
    return ProductService(api_client)
