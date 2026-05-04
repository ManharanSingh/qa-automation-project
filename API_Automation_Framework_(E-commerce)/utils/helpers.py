import json
import os

def safe_json(response):
    try:
        return response.json()
    except ValueError:
        return {}

def load_test_data(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Test data file not found: {file_path}")

    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)

def assert_response_time(response, threshold=3):
    response_time = response.elapsed.total_seconds()
    assert response_time < threshold, f"API too slow: {response_time}s"
