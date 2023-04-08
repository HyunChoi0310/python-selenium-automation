from behave import given, when, then
from time import sleep
from selenium.webdriver.common.by import By

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


@when('Click on search button')
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
    context.app.cart_page.verify_cart_empty(expected_text)


@given('Open http://www.amazon.com product page')
def open_amazon_product_page(context):
    context.app.main_page.open_product()


@when('Click add to cart')
def amazon_click_add_to_cart(context):
    context.app.click_page.click_add_to_cart()
    sleep(4)


@when('Store the product name')
def amazon_store_product_name(context):
    context.expected_text = context.app.store_page.store_product_name()

@when('Store the count on the cart basket')
def amazon_store_product_count(context):
    context.expected_count = context.app.store_page.store_cart_count()


@when('Click no on popup window')
def click_no_popup(context):
    context.app.click_page.click_popup_no_thank()
    sleep(4)
    context.app.click_page.click_popup_x_mark()    sleep(4)


@then('Click go to cart')
def amazon_click_go_to_cart(context):
    context.app.click_page.click_go_to_cart()
    sleep(10)


@then('Verify the cart number {expected_count} added')
def amazon_verify_cart_count(context, expected_count):
    context.app.cart_page.verify_cart_count(expected_count)


@then('Verify the correct product name displayed')
def amazon_verify_product_name(context):
    expected_text = context.expected_text
    context.app.cart_page.verify_product_name(expected_text)


@when('Hover over language options')
def hover_lang_options(context):
    context.app.header.hover_lang_options()


@then('Verify spanish is present')
def amazon_verify_lang_shown(context):
    context.app.header.verify_lang_shown()


@when('Select department by alias {alias}')
def amazon_select_department(context, alias):
    context.app.header.select_department(alias)


@then('Verify {category} department is selected')
def amazon_verify_department_selected(context, category):
    context.app.search_result_page.verify_department_selected(category)


@given('Open Amazon product from the closing category')
def amazon_product_closing_category(context):
    context.app.main_page.open_product_closing_category()


@when('Hover over New Arrivals')
def amazon_hover_new_arrival(context):
    context.app.header.hover_new_arrival()


@then('Verify that user can see the deals')
def amazon_verify_deals_shown(context):
    context.app.search_result_page.verify_deals_shown()