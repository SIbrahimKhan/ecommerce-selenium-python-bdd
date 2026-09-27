# 🛒 E-Commerce Selenium BDD Test Automation Framework
A **Python + Selenium + Behave (BDD)** test automation framework built
against [saucedemo.com](https://www.saucedemo.com), covering **login, cart,
checkout, and product sorting** flows using the **Page Object Model**,
data-driven Gherkin scenarios, environment-based configuration, and
automatic failure screenshots.

This project is built to demonstrate test **framework design** — not just a
handful of test scripts — the same architecture patterns used in real
production QA automation suites.

---

## 📖 Table of Contents

- [Why this project exists](#-why-this-project-exists)
- [Architecture](#-architecture)
- [Project structure](#-project-structure)
- [Setup](#-setup)
- [Running tests](#-running-tests)
- [Configuration](#-configuration)
- [Scenarios covered](#-scenarios-covered)
- [Engineering decisions & gotchas solved](#-engineering-decisions--gotchas-solved)
- [Roadmap](#-roadmap)
- [Tech stack](#-tech-stack)
- [License](#-license)

---

## 🎯 Why this project exists

| Capability | What it demonstrates |
|---|---|
| **Page Object Model (POM)** | UI logic (locators, actions) is fully separated from test logic — a redesigned page only requires updating one file |
| **BDD with Gherkin** | Scenarios are readable by non-technical stakeholders, not just engineers |
| **Data-driven testing** | `Scenario Outline` + `Examples` tables cover multiple inputs — including boundary and negative cases — from one template |
| **Config-driven environments** | Swap `qa` / `staging` via a single `ENV` variable, zero code changes |
| **Automatic failure screenshots** | Captured via Behave hooks the moment a scenario fails — visual evidence, not just a stack trace |
| **Tagged execution** | `@smoke`, `@regression`, `@e2e`, `@negative` — run a fast subset in CI, full regression on demand |

---

## 📁 Project structure

```
ecommerce-selenium-python-bdd/
├── features/
│   ├── login.feature
│   ├── cart_checkout.feature
│   ├── product_sort.feature
│   ├── environment.py          # Behave hooks: driver lifecycle, screenshots
│   └── steps/
│       ├── common_steps.py
│       ├── login_steps.py
│       ├── cart_checkout_steps.py
│       └── product_sort_steps.py
├── pages/                      # Page Object Model classes
│   ├── base_page.py
│   ├── login_page.py
│   ├── inventory_page.py
│   ├── cart_page.py
│   └── checkout_page.py
├── utils/
│   ├── driver_factory.py       # Chrome driver creation & options
│   └── config_reader.py        # Reads config.yaml, supports ENV override
├── config/
│   └── config.yaml
├── requirements.txt
└── .gitignore
```

---

## ⚙️ Setup

```bash

python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

pip install -r requirements.txt
```

> ChromeDriver does **not** need to be downloaded manually —
> `webdriver-manager` automatically fetches the version matching your
> installed Chrome.

---

## ▶️ Running tests

```bash
# Run everything
behave

# Run only smoke tests
behave --tags=@smoke

# Run only regression tests
behave --tags=@regression

# Run a single feature file
behave features/login.feature

# Run against a different environment defined in config.yaml
ENV=staging behave
```

---

## 🔧 Configuration

Environment, browser, and wait settings live in `config/config.yaml`:

```yaml
environment: qa

qa:
  base_url: "https://www.saucedemo.com/"
  browser: "chrome"
  headless: true
  implicit_wait: 5
  explicit_wait: 10
```

Test user credentials for saucedemo's built-in demo accounts
(`standard_user`, `locked_out_user`, `problem_user`, etc.) are also defined
here — kept out of feature files and step definitions entirely, so nothing
sensitive is hardcoded in test logic.

---

## ✅ Scenarios covered

| Feature | Scenarios |
|---|---|
| **Login** | Valid login · locked-out user · invalid credential combinations (data-driven via `Scenario Outline`) |
| **Cart** | Add single/multiple products · remove item · verify cart badge count |
| **Checkout** | Full end-to-end checkout through to order confirmation · missing-field validation |
| **Sorting** | Verify products are correctly ordered by ascending/descending price |

---

## 🧠 Engineering decisions & gotchas solved

Real issues hit and deliberately solved while building this — useful context
if you extend the framework:

- **Empty-string matching in `Scenario Outline`s** — Behave's default `{}`
  placeholder requires at least one character, which breaks negative test
  cases passing an empty username/password. A custom `MaybeEmpty` parse type
  is registered in `features/environment.py` to allow zero-length matches.
- **Headless window sizing** — `--start-maximized` is silently ignored in
  headless Chrome. The driver factory explicitly sets `--window-size`
  instead when running headless, to keep elements consistently visible.
- **Chrome's "Change your password" data-breach popup** — saucedemo's
  well-known public test password sometimes triggers Chrome's native
  leaked-password warning, which intercepts clicks mid-test. Disabled via
  the `profile.password_manager_leak_detection` Chrome preference in
  `utils/driver_factory.py`.
- **Asserting on absence, not presence** — confirming a cart is *empty*
  requires a non-waiting element lookup. Selenium's explicit-wait helpers
  are built to wait for elements to *appear*, so using them to prove
  something is *absent* just times out instead of asserting correctly.
- **Implicit + explicit wait conflict** — mixing a global implicit wait with
  per-call explicit waits causes unpredictable, intermittent timeouts, since
  every internal lookup inside an explicit wait's polling loop also becomes
  subject to the implicit wait. This project uses **explicit waits only**.

---

## 🗺 Roadmap

- [ ] API validation layer (`requests`) — cross-check UI-displayed data
      against backend responses
- [ ] Docker + Selenium Grid for parallel/cross-browser execution
- [ ] GitHub Actions CI pipeline running the smoke suite on every push
- [ ] Allure reporting for richer HTML test reports

---

## 🧰 Tech stack

| Layer | Tool |
|---|---|
| Language | Python 3.11 |
| Browser automation | Selenium WebDriver |
| BDD | Behave |
| Driver management | webdriver-manager |
| Config | PyYAML |
