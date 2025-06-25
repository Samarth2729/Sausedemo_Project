# 🧪 SauceDemo UI Test Automation with Playwright & Pytest

This project automates the end-to-end checkout flow of the [SauceDemo](https://www.saucedemo.com) e-commerce demo site using **Playwright** with **Pytest** in Python.

## ✅ Test Covered

- Login to the application
- Add item to cart
- Assert cart badge shows correct count
- Verify product name in the cart
- Complete the checkout form
- Validate total price
- Confirm successful order message

## 📄 Test File

`Task_2.py`

```bash
pytest test_login_add_checkout.py
```
## 🧰 Tech Stack
- 🎭 Playwright (Python)
- 🧪 Pytest
- 🐍 Python 3.13

## 📦 Installation

```bash
pip install playwright pytest
playwright install
```
## 📝 Notes
- Script uses XPath locators for precision
- time.sleep() is used for demo waits; replace with better waits if needed

## 📧 Author
**Samarth Rathore**
📎 [Test Video Proof](https://drive.google.com/file/d/1z9BAxry6zQdPXATFuTIgy85_zDFgaQco/view?usp=sharing)


