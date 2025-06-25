import pytest
from playwright.sync_api import sync_playwright, expect
import time


def test_login_add_checkout():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        # Step 1: Login
        page.goto("https://www.saucedemo.com/")
        page.wait_for_load_state("networkidle")
        page.locator("//input[@id='user-name']").fill("standard_user")
        page.locator("//input[@id='password']").fill("secret_sauce")
        page.locator("//input[@id='login-button']").click()

        page.wait_for_load_state("networkidle")
        expect(page).to_have_title("Swag Labs")

        # Step 2: Cart

        page.locator("//button[@id='add-to-cart-sauce-labs-backpack']").click()

        # Assert cart badge shows 1
        cart_badge = page.locator("//span[@class='shopping_cart_badge']")
        expect(cart_badge).to_have_text("1")
        time.sleep(5)

        # Assert Product name

        page.locator("//a[@class='shopping_cart_link']").click()
        page.wait_for_load_state("networkidle")

        product_name = page.locator("//div[@class='inventory_item_name']")
        expect(product_name).to_have_text("Sauce Labs Backpack")

        time.sleep(5)

        # Step 3: Checkout

        page.locator("//button[@id='checkout']").click()
        page.wait_for_load_state("networkidle")

        page.locator("//input[@id='first-name']").fill("sam")
        page.locator("//input[@id='last-name']").fill("rathore")
        page.locator("//input[@id='postal-code']").fill("12345")

        page.locator("//input[@id='continue']").click()
        time.sleep(5)

        # Assert Total Price
        total_price = page.locator("//div[@class='summary_total_label']")
        expect(total_price).to_have_text("Total: $32.39")

        page.locator("//button[@id='finish']").click()
        page.wait_for_load_state("networkidle")

        # Assert Thankyou Message
        thank_you = page.locator("//h2[normalize-space()='Thank you for your order!']")
        expect(thank_you).to_have_text("Thank you for your order!")
        time.sleep(5)

        browser.close()











