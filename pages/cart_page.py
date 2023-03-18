from behave import given, when, then
from selenium.webdriver.common.by import By
from pages.base_page import Page

class CartPage(Page):

    CART_EMPTY_TEXT = (By.CSS_SELECTOR, '.a-row.sc-your-amazon-cart-is-empty h2')
    PRODUCT_NAME_CART = (By.CSS_SELECTOR, '.a-truncate.sc-grid-item-product-title.a-size-base-plus .a-truncate-cut')
    CART_COUNT = (By.CSS_SELECTOR, '#nav-cart-count')

    def verify_cart_empty(self, expected_text):
        self.verify_text(expected_text, *self.CART_EMPTY_TEXT)


    def verify_product_name(self, expected_text):
        self.verify_text_contains(expected_text, *self.PRODUCT_NAME_CART)


    def verify_cart_count(self, expected_count):
        self.verify_count(expected_count, *self.CART_COUNT)