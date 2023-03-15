from selenium.webdriver.common.by import By
from pages.base_page import Page

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class StorePage(Page):
    PRODUCT_NAME = (By.CSS_SELECTOR, "span#productTitle")
    CART_COUNT = (By.CSS_SELECTOR, "#nav-cart-count")

    def store_product_name(self):
        return self.store_name(*self.PRODUCT_NAME)

    def store_cart_count(self):
        return self.store_count(*self.CART_COUNT)