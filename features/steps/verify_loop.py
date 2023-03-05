from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

COLOR_OPTIONS = (By.CSS_SELECTOR, "#variation_color_name li")
SELECTED_COLOR = (By.CSS_SELECTOR, "span.selection")

INPUT_PRODUCT = (By.CSS_SELECTOR, "input#twotabsearchtextbox")
SEARCH_BUTTON = (By.CSS_SELECTOR, "input#nav-search-submit-button")
PRODUCT_RESULT = (By.CSS_SELECTOR, "img.s-image")
#PRODUCT_RESULT = (By.CSS_SELECTOR, ".a-color-state.a-text-bold")
ALL_IMAGES = (By.CSS_SELECTOR, "span.rush-component.s-latency-cf-section  img.s-image")
ALL_PRODUCTS_NAME = (By.CSS_SELECTOR, "span.rush-component.s-latency-cf-section h2 a")

@given('Open Amazon product {product_id} page')
#@given('Open Amazon product B096VQ1BQX page')
def open_product_page(context, product_id):
    context.driver.get(f'https://www.amazon.com/gp/product/{product_id}/')


@then('Verify that color has been selected by clicking')
def click_each_color(context):
    context.driver.find_element(*COLOR_OPTIONS).click()

    all_color_options = context.driver.find_elements(*COLOR_OPTIONS)
#    print(f'{all_color_options}')

    expected_selected_colors = ['1577 Blue', '1588 Black', '2126 Blue', '2127 Blue']
    actual_selected_colors = []
    for color in all_color_options[:4:]:
        color.click()
        selected_color = context.driver.find_element(*SELECTED_COLOR).text
        print(f'{selected_color},')
        actual_selected_colors += [selected_color]

    assert expected_selected_colors == actual_selected_colors, f'Expected : {expected_selected_colors}, but got {actual_selected_colors}'


@when('Search coffee maker product')
#@when('Search {product_name} product')
def search_product(context):
    context.driver.find_element(*INPUT_PRODUCT).send_keys("coffee maker")
    context.driver.find_element(*SEARCH_BUTTON).click()


@then('Verify correct product name and image')
def verify_name_image(context):
    context.driver.wait.until(EC.presence_of_element_located(PRODUCT_RESULT))
#    context.driver.get('https://www.amazon.com/s?k=coffee+maker&crid=2AKCT6PZFGAZO&sprefix=%2Caps%2C620&ref=nb_sb_ss_recent_1_0_recent')
    all_images = context.driver.find_elements(*ALL_IMAGES)
#    print(f'all image: {all_images}')
    all_products_name = context.driver.find_elements(*ALL_PRODUCTS_NAME)
#    print(f'all products_name: {all_products_name}')

    assert len(all_images) == len(all_products_name), f'Count of images :{len(all_images)} Count of products_name : {len(all_products_name)}'