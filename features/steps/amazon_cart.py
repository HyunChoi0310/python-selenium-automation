import time

from selenium.webdriver.common.by import By
from behave import given, when, then

@given('Open Amazon page1')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')


@when('Click for cart 0 on amazon')
def search_product(context):
    time.sleep(2)
    context.driver.find_element(By.CSS_SELECTOR, "a[id='nav-cart']").click()

@then('User verify cart for empty')
def verify_search_result(context):
    expected_result = "Your Amazon Cart is empty"
    actual_result = context.driver.find_element(By.CSS_SELECTOR, "h2").text
    assert expected_result == actual_result, f'Expected {expected_result} but got {actual_result}'

