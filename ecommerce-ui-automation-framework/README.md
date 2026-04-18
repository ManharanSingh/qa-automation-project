# E-commerce UI Automation Framework

A scalable **QA Automation Framework** built using **Selenium, Pytest, and Page Object Model (POM)** to automate end-to-end user workflows of a real-world web application.

---

## Overview

This framework automates critical user journeys of the SauceDemo application, focusing on reliability, maintainability, and real-world automation practices.

### Covered Workflows:

* User Login (Valid & Invalid scenarios)
* Product Add to Cart
* Cart Management (Remove items)
* End-to-End Checkout Process

---

## Tech Stack

* **Python**
* **Selenium WebDriver**
* **Pytest**
* **Page Object Model (POM)**
* **Custom Logging System**
* **Pytest HTML Reports**
* **GitHub Actions (CI/CD)**

---

## Key Features

* Modular Page Object Model design
* Reusable BasePage for common actions
* Config-based test data management
* Parametrized test execution
* Automatic screenshot capture on test failure
* TML test reporting
* CI integration with GitHub Actions

---

## Project Structure

```
ecommerce-ui-automation-framework/
│
├── pages/          # Page Object classes
├── tests/          # Test cases
├── utils/          # BasePage & Logger
├── config/         # Configurations
├── reports/        # Test reports
├── screenshots/    # Failure screenshots
├── logs/           # Execution logs
├── conftest.py     # Pytest fixtures & hooks
└── requirements.txt
```

---

## How to Run Tests

### 1. Install dependencies

```
pip install -r requirements.txt
```

### 2. Run tests

```
pytest -v
```

### 3. Generate HTML report

```
pytest --html=reports/report.html
```

---

## Test Scenarios

* ✅ Valid Login
* ❌ Invalid Login (Locked User)
* 🛒 Add Product to Cart
* ❌ Remove Product from Cart
* 💳 Complete Checkout Flow

---

## Reporting & Screenshots

* HTML reports generated after execution
* Screenshots automatically captured on test failure
* Logs stored for debugging and traceability

---

## CI/CD Integration

This project uses **GitHub Actions** to automatically run tests on every push.

---

## Key Learnings

* Designing scalable automation frameworks
* Implementing reusable test architecture
* Handling synchronization using explicit waits
* Improving debugging using logs and reports
* Integrating automation with CI pipelines

---

## Future Enhancements

* API Automation Integration
* Cross-browser execution
* Data-driven testing using external files
* Parallel test execution

---

## 👨‍💻 Author

**Manharan Singh**

