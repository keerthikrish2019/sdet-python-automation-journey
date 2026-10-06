# SDET Automation Framework

A Python-based test automation framework demonstrating API and UI automation using pytest, Requests, and Playwright.

## Key Features

- API automation using Requests
- UI automation using Playwright
- Pytest test framework
- Reusable API client
- Page Object Model (POM)
- Test data factories
- Pytest fixtures
- Environment-based configuration
- Logging and failure diagnostics
- HTML test reporting
- CI/CD integration with GitHub Actions

## Project Structure

```text
sdet-automation-framework/
│
├── api/
│   └── api_client.py
│
├── pages/
│   ├── login_page.py
│   └── dashboard_page.py
│
├── data/
│   └── user_factory.py
│
├── tests/
│   ├── test_api.py
│   └── test_ui.py
│
├── config.py
├── conftest.py
├── requirements.txt
├── .gitignore
└── README.md