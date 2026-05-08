import pytest
from utils.api_client import APIClient
from services.product_service import ProductService
from config.config import Config

@pytest.fixture(scope="session")
def api_client():
    return APIClient(base_url=Config.get_base_url())

@pytest.fixture
def product_service(api_client):
    return ProductService(api_client)
