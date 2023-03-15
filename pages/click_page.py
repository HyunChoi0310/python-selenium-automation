from selenium.webdriver.common.by import By
from pages.base_page import Page

class ClickPage(Page):
    CLICK_ORDER = (By.CSS_SELECTOR, '#nav-orders')
    CLICK_CART_ICON = (By.CSS_SELECTOR, 'span.nav-cart-icon.nav-sprite')

    ADD_TO_CART = (By.CSS_SELECTOR, "#add-to-cart-button")
    GO_TO_CART = (By.CSS_SELECTOR, "#nav-cart")

    def click_order(self):
        self.click(*self.CLICK_ORDER)

    def click_cart_icon(self):
        self.click(*self.CLICK_CART_ICON)

    def click_add_to_cart(self):
        self.click(*self.ADD_TO_CART)

    def click_go_to_cart(self):
        self.click(*self.GO_TO_CART)