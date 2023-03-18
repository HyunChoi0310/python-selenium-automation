from pages.main_page import MainPage
from pages.header import Header
from pages.search_result_page import SearchResultPage
from pages.click_page import ClickPage
from pages.store_page import StorePage
from pages.base_page import Page
from pages.cart_page import CartPage

class Application:

    def __init__(self, driver):
        self.driver = driver
        self.main_page = MainPage(self.driver)
        self.header = Header(self.driver)
        self.search_result_page = SearchResultPage(self.driver)
        self.click_page = ClickPage(self.driver)
        self.store_page = StorePage(self.driver)
        self.base_page = Page(self.driver)
        self.cart_page = CartPage(self.driver)