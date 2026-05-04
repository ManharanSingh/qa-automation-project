class ProductService:
    """
    Service layer for Product API operations.
    """

    def __init__(self, client):
        self.client = client

    def get_all_products(self, params=None):
        return self.client.get("/products", params=params, expected_status=200)

    def get_product(self, product_id):
        if not isinstance(product_id, int):
            raise ValueError("product_id must be an integer")

        return self.client.get(f"/products/{product_id}", expected_status=200)

    def get_product_unvalidated(self, product_id):
        if not isinstance(product_id, int):
            raise ValueError("product_id must be an integer")

        return self.client.get(f"/products/{product_id}")
