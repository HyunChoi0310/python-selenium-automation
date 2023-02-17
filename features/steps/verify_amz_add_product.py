from selenium.webdriver.common.by import By
from behave import given, when, then

@given('Open http://www.amazon.com product page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/dp/B074W8DJ1Y/ref=sspa_dk_detail_4?psc=1&pd_rd_i=B074W8DJ1Y&pd_rd_w=LLfSy&content-id=amzn1.sym.dd2c6db7-6626-466d-bf04-9570e69a7df0&pf_rd_p=dd2c6db7-6626-466d-bf04-9570e69a7df0&pf_rd_r=RDSR96PCJBYY7ZYE6PKS&pd_rd_wg=1xldH&pd_rd_r=679b03f4-59bb-46bb-9131-77b892088de4&s=apparel&sp_csd=d2lkZ2V0TmFtZT1zcF9kZXRhaWxfdGhlbWF0aWM&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExUUNQNjRXSDQ0VFUmZW5jcnlwdGVkSWQ9QTA4MTM2MDMyTzI5TVAzWlJEOVVVJmVuY3J5cHRlZEFkSWQ9QTA4NTcxMzhKTkRWTlYxNVQ0VlEmd2lkZ2V0TmFtZT1zcF9kZXRhaWxfdGhlbWF0aWMmYWN0aW9uPWNsaWNrUmVkaXJlY3QmZG9Ob3RMb2dDbGljaz10cnVl')

@when('Click add to cart')
def click_product(context):
    context.driver.find_element(By.CSS_SELECTOR, "#add-to-cart-button").click()

@then('The number on the cart is added')
def number_on_cart(context):
    expected_text = "Added to Cart"
    actual_text = context.driver.find_element(By.CSS_SELECTOR, "span.a-size-medium-plus.a-color-base").text
    assert actual_text == expected_text, f'Expected {expected_text} but got {actual_text}'
