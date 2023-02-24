from time import sleep

from selenium.webdriver.common.by import By
from behave import given, when, then

BESTSELLER_HEADER = (By.CSS_SELECTOR, "._p13n-zg-nav-tab-all_style_zg-tabs__EYPLq li")
CUSTOMER_SERVICE = (By.CSS_SELECTOR, "a[data-csa-c-slot-id='nav_cs_3']")
CUSTOMER_SERVICE_PAGE = (By.CSS_SELECTOR, "h1.fs-heading.bolded")
CUSTOMER_SERVICE_LINKS = (By.CSS_SELECTOR, "div.issue-card-wrapper")
CUSTOMER_SERVICE_HELP = (By.CSS_SELECTOR, "div.page-container label h2")
CUSTOMER_INPUT = (By.CSS_SELECTOR, "input#hubHelpSearchInput")
#CUSTOMER_HELP_TOPIC = (By.CSS_SELECTOR, "div.page-container h2"[1])
CUSTOMER_HELP_TOPIC = (By.XPATH, '//*[@id="hub-gateway-app-unauth"]/div[2]/div/h2')

@given('Open Amazon bestseller page')
def open_amazon(context):
    sleep(3)
    context.driver.get('https://www.amazon.com/gp/bestsellers/?ref_=nav_cs_bestsellers')

@then('Verify {expected_amount} links on the header')
def verify_header_5links(context, expected_amount):
    sleep(3)
#    print("\n before Expected amount:", type(expected_amount))
    expected_amount = int(expected_amount)
#    print("\n after Expected amount:", type(expected_amount))
    header_links = context.driver.find_elements(*BESTSELLER_HEADER)

#   print("\n header_links:", type(len(header_links)))
    assert len(header_links) == expected_amount, f'Expected is {expected_amount},but got {len(header_links)}'

@when('Click Amazon Customer Service page')
def click_customer_service_page(context):
    sleep(3)
    context.driver.find_element(*CUSTOMER_SERVICE).click()

@then('Verify Customer Service is visible')
def verify_customer_service_visible(context):
    sleep(3)
    expected_customer = "Welcome to Amazon Customer Service"
    actual_customer = context.driver.find_element(*CUSTOMER_SERVICE_PAGE).text
    assert actual_customer == expected_customer, f'Expected {expected_customer} but got {actual_customer}'

@then('Verify Customer Service {expected_customer_links} links')
def verify_customer_links(context, expected_customer_links):
    sleep(3)
    expected_customer_links = int(expected_customer_links)
    customer_service_links = context.driver.find_elements(*CUSTOMER_SERVICE_LINKS)
    print("\n Exp links",expected_customer_links, type(expected_customer_links))
    print("\n Act links", len(customer_service_links), type(len(customer_service_links)))
    print("\n Act links", customer_service_links)
    assert len(customer_service_links) == expected_customer_links, f'Expected {expected_customer_links} but got {len(customer_service_links)}'

@then('Verify Customer Service Help is visible')
def verify_help_visible(context):
    sleep(3)
    expected_help = "Search our help library"
    actual_help = context.driver.find_element(*CUSTOMER_SERVICE_HELP).text
    assert actual_help == expected_help, f'Expected {expected_help} but got {actual_help}'

@then('Verify Customer Service Input_Field is present')
def verify_input_field_present(context):
    sleep(3)
    assert context.driver.find_element(*CUSTOMER_INPUT).is_displayed()

@then('Verify Customer Service Help Topic is visible')
def verify_help_topic_visible(context):
    sleep(3)
    expected_topic = "All help topics"
    actual_topic = context.driver.find_element(*CUSTOMER_HELP_TOPIC).text
    print("\n Help Topic :", actual_topic)

    assert actual_topic == expected_topic, f'Expected {expected_topic} but got {actual_topic}'