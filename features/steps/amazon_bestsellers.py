from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

BESTSELLERS_LINKS = (By.CSS_SELECTOR, 'div._p13n-zg-nav-tab-all_style_zg-tabs__EYPLq ul li a')

@given('Open Amazon best sellers page')
def open_amazon_bestsellers(context):
    context.driver.get('https://www.amazon.com/gp/bestsellers/?ref_=nav_cs_bestsellers')

@then('User sees {expected_amount} best sellers links')
def verify_5bestsellers_links(context, expected_amount):
    expected_amount = int(expected_amount)  # '5' => 5
    links = context.driver.find_elements(*BESTSELLERS_LINKS)
#   print(links)

    assert len(links) == expected_amount, \
        f'Expected {expected_amount} links but got {len(links)}'
