import pytest
from utils.api_client import APIClient
from services.product_service import ProductService
import os

ENV = os.getenv("ENV", "local")

if ENV == 'ci':
    BASE_URL = "https://dummyjson.com"
else:
    BASE_URL = "https://fakestoreapi.com"

@pytest.fixture(scope="session")
def api_client():
    return APIClient(base_url=BASE_URL)

@pytest.fixture
def product_service(api_client):
    return ProductService(api_client)
