from behave import given, when, then
from time import sleep

from pages.main_page import MainPage
from pages.header import Header
from pages.click_page import ClickPage

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

@given('Open Amazon page')
def open_amazon(context):
    context.app.main_page.open_main()


@when('Input text {text}')
def amazon_input_search(context, text):
    context.app.header.input_search_text(text)


@when('click on search button')
def amazon_click_btn(context):
    context.app.header.click_search()


@then('verify that text {expected_text} is shown')
def amazon_verify_result(context, expected_text):
    context.app.search_result_page.verify_search_result(expected_text)


@when('Click Amazon Orders link')
def amazon_click_order(context):
    context.app.click_page.click_order()


@then('Verify {expected_text} page is opened')
def amazon_verify_signin(context, expected_text):
    context.app.search_result_page.verify_search_result_signin(expected_text)


@when('Click on cart icon')
def amazon_click_cart_icon(context):
    context.app.click_page.click_cart_icon()


@then('Verify {expected_text} text present')
def amazon_verify_cart_empty(context, expected_text):
    context.app.search_result_page.verify_cart_empty(expected_text)


@given('Open http://www.amazon.com product page')
def open_amazon_product_page(context):
    context.app.main_page.open_product()


@when('Click add to cart')
def amazon_click_add_to_cart(context):
    context.app.click_page.click_add_to_cart()
    sleep(10)


@when('Store the product name')
def amazon_store_product_name(context):
    context.expected_text = context.app.store_page.store_product_name()

@when('Store the count on the cart basket')
def amazon_store_product_count(context):
    context.expected_count = context.app.store_page.store_cart_count()


@then('Click go to cart')
def amazon_click_go_to_cart(context):
    context.app.click_page.click_go_to_cart()
    sleep(10)


@then('Verify the cart number {expected_count} added')
def amazon_verify_cart_count(context, expected_count):
    context.app.search_result_page.verify_cart_count(expected_count)


@then('Verify the correct product name displayed')
def amazon_verify_product_name(context):
    expected_text = context.expected_text
    context.app.search_result_page.verify_product_name(expected_text)