from selenium.webdriver.common.by import By
from pages.base_page import Page

class ClickPage(Page):
    CLICK_ORDER = (By.CSS_SELECTOR, '#nav-orders')
    CLICK_CART_ICON = (By.CSS_SELECTOR, 'span.nav-cart-icon.nav-sprite')
    CLICK_NO_THANK = (By.CSS_SELECTOR, '.a-button-input[aria-labelledby="attachSiNoCoverage-announce"]')
    CLICK_X_MARK = (By.CSS_SELECTOR, '#attach-close_sideSheet-link[aria-label="Exit this panel and return to the product page. "]')

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

    def click_popup_no_thank(self):
        self.click(*self.CLICK_NO_THANK)

    def click_popup_x_mark(self):
        self.click(*self.CLICK_X_MARK)