import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
from utils.logger import get_logger

logger = get_logger(__name__)

class APIClient:
    """
    Reusable HTTP client for API testing with retry, logging, and validation support.
    """

    def __init__(self, base_url, headers=None, timeout=5):
        self.base_url = base_url
        self.timeout = timeout

        self.session = requests.Session()
        self.session.headers.update(headers or {})
        self.session.headers.setdefault("Content-Type", "application/json")

        # Fix for Cloudflare blocking (CI environments)
        self.session.headers.setdefault(
            "User-Agent",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
        )
        retries = Retry(
            total=3,
            backoff_factor=0.5,
            status_forcelist=[500, 502, 503, 504],
            allowed_methods=["GET", "POST", "PUT", "DELETE", "PATCH"],
            raise_on_status=False
        )

        adapter = HTTPAdapter(max_retries=retries)
        self.session.mount("http://", adapter)
        self.session.mount("https://", adapter)

    def request(self, method, endpoint, expected_status=None, raise_for_status=False, **kwargs):
        url = f"{self.base_url.rstrip('/')}/{endpoint.lstrip('/')}"

        try:
            logger.info(f"{method.upper()} {url}")

            if "json" in kwargs:
                logger.info(f"Payload: {kwargs['json']}")

            if "params" in kwargs:
                logger.info(f"Query Params: {kwargs['params']}")

            timeout = kwargs.pop("timeout", self.timeout)

            response = self.session.request(
                method=method,
                url=url,
                timeout=timeout,
                **kwargs
            )

            logger.info(
                f"Response: {response.status_code} | Time: {response.elapsed.total_seconds()}s"
            )

            logger.debug(f"Headers: {self.session.headers}")

            if response.status_code >= 400:
                logger.error(f"Response Body: {response.text[:500]}")

            if expected_status and response.status_code != expected_status:
                raise AssertionError(
                    f"{method.upper()} {endpoint} | Expected {expected_status}, "
                    f"Got {response.status_code} | Response: {response.text}"
                )

            if raise_for_status:
                response.raise_for_status()

            return response

        except requests.exceptions.RequestException as e:
            logger.error(f"Request failed: {str(e)}")
            raise

    def get(self, endpoint, **kwargs):
        return self.request("get", endpoint, **kwargs)

    def post(self, endpoint, **kwargs):
        return self.request("post", endpoint, **kwargs)

    def put(self, endpoint, **kwargs):
        return self.request("put", endpoint, **kwargs)

    def delete(self, endpoint, **kwargs):
        return self.request("delete", endpoint, **kwargs)
