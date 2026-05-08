import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    ENV = os.getenv("ENV", "local")

    BASE_URLS = {
        "local": os.getenv("LOCAL_BASE_URL"),
        "ci": os.getenv("CI_BASE_URL"),
        "staging": os.getenv("STAGING_BASE_URL"),
        "prod": os.getenv("PROD_BASE_URL"),
    }

    @classmethod
    def get_base_url(cls):
        base_url = cls.BASE_URLS.get(cls.ENV)

        if not base_url:
            raise ValueError(f"Invalid ENV: {cls.ENV}")

        return base_url
