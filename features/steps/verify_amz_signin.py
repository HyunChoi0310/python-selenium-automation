from selenium.webdriver.common.by import By
from behave import given, when, then

@given('Open https://www.amazon.com')
def open_amazon(context):
    context.driver.get('https://www.amazon.com')

@when('Click Orders')
def click_orders(context):
    context.driver.find_element(By.CSS_SELECTOR, "#nav-orders").click()

@then('Sign In header is visible')
def header_visible(context):
    expected_title = "Sign in"
    actual_title = context.driver.find_element(By.CSS_SELECTOR, "h1.a-spacing-small").text
    assert actual_title == expected_title, f'Expected {expected_title} but got{actual_title}'

@then('email input field is present')
def email_present(context):
    assert context.driver.find_element(By.CSS_SELECTOR, "#ap_email").is_displayed()
