<h1 align="center">🧃 OWASP Juice Shop - Test Automation Framework</h1>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue.svg?logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Pytest-Testing_Framework-yellow.svg?logo=pytest&logoColor=white" alt="Pytest">
  <img src="https://img.shields.io/badge/Playwright-UI_Automation-2EAD33.svg?logo=playwright&logoColor=white" alt="Playwright">
  <img src="https://img.shields.io/badge/Requests-API_Automation-red.svg" alt="Requests">
  <img src="https://img.shields.io/badge/Allure-Reporting-9cf.svg" alt="Allure">
  <img src="https://img.shields.io/badge/Docker-Local_Testing-2496ED.svg?logo=docker&logoColor=white" alt="Docker">
</p>

<p align="center">
  <i>A modern, scalable, and robust test automation framework designed to test the OWASP Juice Shop application across UI, API, and BDD layers.</i>
</p>

---

## 🚀 Tech Stack

- **Language:** Python 3.10+
- **Test Runner:** Pytest
- **UI Automation:** Playwright (Sync API) — fast, reliable, and native network interception.
- **API Automation:** Requests + `jsonschema` — for rigid contract testing.
- **BDD:** Pytest-BDD — bridging the gap between business and engineering with Gherkin.
- **Test Data:** Faker — generating unique users dynamically.
- **Reporting:** Allure Report — interactive dashboards with automatic screenshots.

## 📁 Architecture (Page Object Model)

```text
JuiceShop_ATF/
├── pages/                  # Page Object classes (Locators & UI actions)
├── tests/
│   ├── api/                # API tests (Auth, CRUD, Contract validation)
│   ├── bdd/                # Gherkin scenarios (.feature) & step definitions
│   ├── ui/                 # Playwright UI tests
│   └── unit/               # Unit tests for internal utilities
├── utils/
│   ├── schemas/            # JSON schemas for API contract testing
│   └── data_generator.py   # Faker utility for test data generation
├── conftest.py             # Global Pytest fixtures (Browser, Allure screenshots)
├── pytest.ini              # Pytest configuration & custom markers
└── requirements.txt        # Project dependencies