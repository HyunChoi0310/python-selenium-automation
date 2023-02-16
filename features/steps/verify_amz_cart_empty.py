from selenium.webdriver.common.by import By
from behave import given, when, then

@given('Open http://www.amazon.com')
def open_amazon(context):
    context.driver.get('https://www.amazon.com')

@when('Click the cart')
def click_cart(context):
    context.driver.find_element(By.CSS_SELECTOR, "span.nav-cart-icon.nav-sprite").click()

@then('Your Amazon Cart is empty is visible')
def cart_empty(context):
    expected_text = "Your Amazon Cart is empty"
    actual_text = context.driver.find_element(By.CSS_SELECTOR, "div.a-row.sc-your-amazon-cart-is-empty h2").text
    assert actual_text == expected_text, f'Expected {expected_text} but got{actual_text}'