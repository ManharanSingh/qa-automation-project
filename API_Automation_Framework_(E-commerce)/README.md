# 🚀 API Automation Framework (E-commerce)

A production-style API automation framework built using Python and Pytest, designed to demonstrate real-world QA Automation practices including structured test design, schema validation, data-driven testing, and reporting.

---

## 📌 Overview

This project tests an e-commerce API (Fake Store API) using a scalable and maintainable automation framework.

It focuses on:

* Clean architecture (Client → Service → Tests)
* Robust validation (JSON schema + business rules)
* Data-driven testing
* Performance checks
* Professional reporting with Allure

---

## 🧱 Tech Stack

* Python
* Pytest
* Requests
* jsonschema
* Allure Reports

---

## 📂 Project Structure

```
api-framework/
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
│
├── data/
│   ├── schemas.py
│   └── test_data.json
│
├── requirements.txt
└── README.md
```

---

## ⚙️ Features

### ✅ API Client

* Centralized request handling
* Retry mechanism with backoff
* Configurable timeout
* Request/response logging
* Status validation support

---

### ✅ Service Layer

* Encapsulates API endpoints
* Improves readability and maintainability
* Supports both validated and unvalidated calls

---

### ✅ Test Design

* Parametrized tests (multiple scenarios)
* Data-driven testing (external JSON)
* Clean separation of test logic and data

---

### ✅ Schema Validation

* JSON schema validation using `jsonschema`
* Enforces:

  * Data types
  * Required fields
  * Business rules (e.g., price > 0)
  * No unexpected fields

---

### ✅ Performance Validation

* Response time assertions included in tests

---

### ✅ Allure Reporting

* Structured test reports
* Step-level visibility
* Severity tagging

---

## 🧪 Sample Test Scenario

* Validate product API with multiple IDs
* Handle valid and invalid cases
* Verify schema + business rules
* Measure response performance

---

## ▶️ How to Run

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 2. Run tests

```bash
pytest
```

---

### 3. Generate Allure results

```bash
pytest --alluredir=allure-results
```

---

### 4. View report

```bash
allure serve allure-results
```

---

## 📊 Example Validations

* Product schema validation
* Price must be greater than 0
* Response must match expected structure
* Invalid product returns empty response

---

## 💡 Key Highlights

* Designed with real-world QA automation practices
* Focus on maintainability and scalability
* Demonstrates strong API testing fundamentals

---

## 📌 Future Improvements

* CI/CD integration (GitHub Actions)
* Docker support
* Extended API coverage (Users, Orders)

---

## 👨‍💻 Author

[Your Name]
Aspiring QA Automation Engineer

---

## ⭐ Final Note

This project focuses on **quality over quantity** — showcasing a single module implemented with strong design, validation, and testing practices aligned with industry expectations.



