# 🚀 API Automation Framework (E-commerce)

A scalable and production-style API automation framework built using Python and Pytest, designed to demonstrate real-world QA Automation practices including framework architecture, schema validation, data-driven testing, environment management, CI integration, and reporting.

---

# 📌 Overview

This project automates testing for e-commerce product APIs using a layered automation framework following industry-style design patterns.

The framework supports:

- Multiple environments (Local + CI)
- Environment-based API switching
- Schema validation
- Data-driven testing
- API performance validation
- Centralized request handling
- CI/CD execution using GitHub Actions
- Professional reporting with Allure

---

# 🧱 Tech Stack

- Python
- Pytest
- Requests
- jsonschema
- Allure Reports
- GitHub Actions
- python-dotenv

---

# 📂 Project Structure

```text
api-framework/
│
├── .github/
│   └── workflows/
│       └── API_testing.yml
│
├── config/
│   └── config.py
│
├── tests/
│   └── test_products.py
│
├── services/
│   └── product_service.py
│
├── utils/
│   ├── api_client.py
│   ├── helpers.py
│   └── logger.py
│
├── data/
│   ├── schemas.py
│   └── test_data.json
│
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

---

# ⚙️ Framework Architecture

```text
Tests
   ↓
Service Layer
   ↓
API Client
   ↓
External API
```

The framework follows separation of concerns to improve maintainability, scalability, and readability.

---

# 🌍 Environment Management

This framework supports multiple environments using `.env` configuration and a centralized config class.

| Environment | API |
|---|---|
| Local | FakeStoreAPI |
| CI | DummyJSON |
| Staging | Configurable |
| Production | Configurable |

Environment switching is handled dynamically without changing test code.

---

# 🔧 Configuration Management

Environment variables are managed using `python-dotenv`.

Example `.env`:

```env
ENV=local

LOCAL_BASE_URL=https://fakestoreapi.com
CI_BASE_URL=https://dummyjson.com
STAGING_BASE_URL=https://dummyjson.com
PROD_BASE_URL=https://fakestoreapi.com
```

---

# ✅ Features

## 🔹 API Client

Centralized reusable HTTP client with:

- Retry mechanism with exponential backoff
- Configurable timeout handling
- Request/response logging
- Status code validation
- Query parameter support
- Session-based request management

---

## 🔹 Service Layer

Encapsulates endpoint logic for cleaner and maintainable test design.

Example:
- `get_all_products()`
- `get_product()`
- `get_product_unvalidated()`

---

## 🔹 Data-Driven Testing

Test scenarios are externalized using JSON test data.

Supports:
- Multiple product IDs
- Positive scenarios
- Negative scenarios

---

## 🔹 Schema Validation

JSON schema validation implemented using `jsonschema`.

Validates:
- Required fields
- Data types
- Business rules
- Flexible response structures across environments

---

## 🔹 Performance Validation

Response time assertions included in tests.

Example:
- API response must complete within threshold time

---

## 🔹 Allure Reporting

Integrated Allure reporting for:

- Step-level reporting
- Severity tagging
- Better debugging visibility
- Professional test reports

---

## 🔹 CI/CD Integration

Integrated with GitHub Actions.

Features:
- Automated test execution on push
- CI-specific environment configuration
- Stable CI execution using environment switching

---

# 🧪 Sample Test Scenarios

## Product API Validation

- Validate product schema
- Validate product data types
- Validate business rules
- Validate invalid product behavior
- Validate API performance

---

# ▶️ How to Run

## 1. Clone Repository

```bash
git clone https://github.com/ManharanSingh/qa-automation-project/tree/main/API_Automation_Framework_(E-commerce)
```

---

## 2. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 3. Configure Environment

Update `.env` if needed.

---

## 4. Run Tests

```bash
pytest
```

---

## 5. Generate Allure Results

```bash
pytest --alluredir=allure-results
```

---

## 6. View Allure Report

```bash
allure serve allure-results
```

---

# 🚀 Running in CI

GitHub Actions automatically runs tests on:
- Push
- Pull Request

CI environment automatically switches to DummyJSON API for stable execution.

---

# 📊 Example Validations

- Product schema validation
- Product ID validation
- Price validation
- Response structure validation
- Negative API validation
- Response time validation

---

# 💡 Key Highlights

- Production-style framework structure
- Multiple environment support
- CI/CD integrated
- Schema-based API validation
- Data-driven testing
- Reusable API client design
- Scalable architecture

---

# 📌 Future Improvements

- Docker support
- API mocking support
- Authentication workflows
- Parallel test execution
- HTML reporting
- API contract testing
- Request/response models

---

# 👨‍💻 Author

Manharan Maravi  
Aspiring QA Automation Engineer

---

# ⭐ Final Note

This project focuses on building a maintainable and scalable API automation framework aligned with real-world QA Automation practices rather than creating large quantities of basic test cases.

The goal is to demonstrate:
- Strong framework design
- Clean test architecture
- Real-world testing practices
- CI/CD awareness
- Maintainable automation code
