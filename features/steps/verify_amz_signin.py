from selenium.webdriver.common.by import By
from behave import given, when, then

from selenium.webdriver.support import expected_conditions as EC

SIGN_IN_BUTTON = (By.CSS_SELECTOR, "#nav-signin-tooltip a.nav-action-button")

@given('Open Amazon page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com')

#@when('Click Orders')
#def click_orders(context):
#    context.driver.find_element(By.CSS_SELECTOR, "#nav-orders").click()

#@then('Sign In header is visible')
#def header_visible(context):
#    expected_title = "Sign in"
#    actual_title = context.driver.find_element(By.CSS_SELECTOR, "h1.a-spacing-small").text
#    assert actual_title == expected_title, f'Expected {expected_title} but got{actual_title}'

#@then('email input field is present')
#def email_present(context):
#    assert context.driver.find_element(By.CSS_SELECTOR, "#ap_email").is_displayed()

@when('Click Sign in from popup')
def popup_signin(context):
    context.driver.wait.until(EC.element_to_be_clickable(SIGN_IN_BUTTON)).click()

@then('Verify Sin in page')
def verify_signin(context):
    context.driver.wait.until(EC.url_contains("https://www.amazon.com/ap/signin"))
    expected_title = "Sign in"
    actual_title = context.driver.find_element(By.CSS_SELECTOR, "h1.a-spacing-small").text
    assert actual_title == expected_title, f'Expected {expected_title} but got{actual_title}'