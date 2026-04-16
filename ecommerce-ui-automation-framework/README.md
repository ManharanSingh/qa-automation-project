# QA Automation Project 
# This project is built as part of my QA Automation learning journey
## overview
This project is an end-to-end QA Automation framework built using **Selenium, Pytest, and Page Object Model (POM)**.

It automates key user flows of the SauceDemo application:

* Login functionality
* Add to cart
* Remove items
* Checkout process

---

## Tech Stack

* Python
* Selenium WebDriver
* Pytest
* Page Object Model (POM)
* Logging & Screenshot handling

---

## Project Structure

```
project/
│
├── pages/          # Page Object classes
│   ├── login_page.py
│   ├── inventory_page.py
│   └── checkout_page.py
│
├── tests/          # Test cases
│   ├── test_login.py
│   ├── test_cart.py
│   └── test_checkout.py
│
├── conftest.py     # Pytest fixtures
├── requirements.txt
└── README.md
```

---

## Features Implemented

* ✔ Login validation (success & failure)
* ✔ Add item to cart
* ✔ Remove item from cart
* ✔ Complete checkout flow
* ✔ Parametrized tests
* ✔ Logging for debugging
* ✔ Screenshot capture on failure

---

## How to Run Tests

### Step 1: Install dependencies
```
pip install -r requirements.txt
```

### Step 2: Run tests

```
python -m pytest -v (for terminal output)
```
python -m pytest --html=report.html ( for html report)
---

## Test Scenarios Covered

* Valid login
* Invalid login (locked user)
* Add product to cart
* Remove product from cart
* Complete purchase flow

---

## Screenshots

(Screenshots are automatically captured on test failure)

---

## Key Learnings

* Building scalable test automation using POM
* Writing reliable tests using explicit waits
* Handling test failures with logging and screenshots
* Structuring projects for real-world QA automation

---

## Future Improvements

* Add API testing integration
* CI/CD pipeline (GitHub Actions)
* Test data externalization (JSON/CSV)
* Cross-browser testing

---

## Author

ManharanSingh
