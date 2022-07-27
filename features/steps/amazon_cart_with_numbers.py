import time

from selenium.webdriver.common.by import By
from behave import given, when, then

@given('Open Amazon page2')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/ap/signin?openid.pape.max_auth_age=900&openid.return_to=https%3A%2F%2Fwww.amazon.com%2Fgp%2Fyourstore%2Fhome%3Fpath%3D%252Fgp%252Fyourstore%252Fhome%26signIn%3D1%26useRedirectOnSuccess%3D1%26action%3Dsign-out%26ref_%3Dnav_AccountFlyout_signout&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0')
    log_in_button = context.driver.find_element(By.CSS_SELECTOR, 'input#ap_email')
    log_in_button.send_keys('hyun.red.cloud@gmail.com')
    continue_button = context.driver.find_element(By.CSS_SELECTOR, 'input#continue')
    continue_button.click()
    password_in_button = context.driver.find_element(By.CSS_SELECTOR, 'input#ap_password')
    password_in_button.send_keys('Tobie0218!!')
    signin_button = context.driver.find_element(By.CSS_SELECTOR, 'input#signInSubmit')
    signin_button.click()

@when('Click for cart with numbers on amazon')
def search_product(context):
    time.sleep(2)
    context.driver.find_element(By.CSS_SELECTOR, 'a[href="/gp/cart/view.html?ref_=nav_cart"]').click()


@then("User verify cart for {expected_num} products")
def step_impl(context, expected_num):
    actual_num = context.driver.find_element(By.XPATH, "//span[@id='nav-cart-count']").text
    assert int(expected_num) == int(actual_num), f'Expected {expected_num} but got {actual_num}'
