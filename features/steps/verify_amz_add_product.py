from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

ADD_TO_CART = (By.CSS_SELECTOR, "#add-to-cart-button")
PRODUCT_NAME = (By.CSS_SELECTOR, "span#productTitle")
PRODUCT_NAME_CART = (By.CSS_SELECTOR, "span.a-truncate-full.a-offscreen")
CART_COUNT = (By.CSS_SELECTOR, "#nav-cart-count")
GO_TO_CART = (By.CSS_SELECTOR, "a[href='/gp/cart/view.html?ref_=sw_gtc']")

@given('Open http://www.amazon.com product page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/Dell-OptiPlex-Computer-Desktop-Keyboard/dp/B09TN242Q5/ref=zg_bs_565098_sccl_3/132-7782273-6146205?psc=1')

@when('Click add to cart')
def click_add_to_cart(context):
    context.driver.find_element(*ADD_TO_CART).click()
    sleep(4)

@when('Store the product name')
def store_product_name(context):
    context.product_name = context.driver.find_element(*PRODUCT_NAME).text
    print(f'Actual count {context.product_name}')

@when('Store the count on the cart basket')
def store_cart_count(context):
    context.actual_count = context.driver.find_element(*CART_COUNT).text
    print(f'Actual count {context.actual_count}')

@then('Click go to cart')
def click_go_cart(context):
    # context.driver.find_element(*GO_TO_CART).click()
    sleep(4)
    context.driver.get('https://www.amazon.com/gp/cart/view.html?ref_=sw_gtc')
    sleep(4)

@then('Verify the correct product name displayed')
def verify_product_name(context):
    actual_product_name = context.driver.find_element(*PRODUCT_NAME_CART).text
    assert actual_product_name in context.product_name[:30], f'Expected product name : {context.product_name} but got {actual_product_name}'

@then('Verify the cart number {expected_count} added')
def varify_cart_count(context, expected_count):
    actual_count = context.driver.find_element(*CART_COUNT).text
    actual_count = int(actual_count)
    assert int(expected_count) == int(actual_count), f'Expected count {expected_count} but got {actual_count}'
