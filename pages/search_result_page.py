from behave import given, when, then
from selenium.webdriver.common.by import By
from pages.base_page import Page


class SearchResultPage(Page):
    SEARCH_RESULT = (By.CSS_SELECTOR, 'span.a-color-state.a-text-bold')
    SEARCH_RESULT_SIGNIN = (By.CSS_SELECTOR, '.a-box h1')
    SUBNAV = (By.CSS_SELECTOR, '#nav-subnav[data-category="{CATEGORY}"]')
    NEW_WOMEN = (By.XPATH, '//img[contains(@src, "AMAZON_FASHION/2022/SITE_FLIPS/SPR_22/SUBNAV/W._CB1648157817_.jpg")]')
    NEW_MEN = (By.XPATH, '//img[contains(@src, "AMAZON_FASHION/2022/SITE_FLIPS/SPR_22/SUBNAV/M._CB1648157817_.jpg")]')
    NEW_GIRLS = (By.XPATH, '//img[contains(@src, "AMAZON_FASHION/2022/SITE_FLIPS/SPR_22/SUBNAV/Girls._CB1648157817_.jpg")]')
    NEW_BOYS = (By.XPATH, '//img[contains(@src, "AMAZON_FASHION/2022/SITE_FLIPS/SPR_22/SUBNAV/Boys._CB1648157817_.jpg")]')
    NEW_BABY = (By.XPATH, '//img[contains(@src, "AMAZON_FASHION/2022/SITE_FLIPS/SPR_22/SUBNAV/Baby._CB1648157817_.jpg")]')
    NEW_LUGGAGE = (By.XPATH, '//img[contains(@src, "AMAZON_FASHION/2020/SUMMER_1/subnav/NA_L.jpg")]')

    def get_selected_locator(self, category):
        return[self.SUBNAV[0], self.SUBNAV[1].replace("{CATEGORY}", category)]

    def verify_search_result(self, expected_text):
        self.verify_text(expected_text, *self.SEARCH_RESULT)

    def verify_search_result_signin(self, expected_text):
        self.verify_text(expected_text, *self.SEARCH_RESULT_SIGNIN)

    def verify_department_selected(self, category):
        locator = self.get_selected_locator(category)
        print("LOcator:", locator)
        self.wait_for_element_appear(*locator)

    def verify_deals_shown(self):
        self.wait_for_element_appear(*self.NEW_WOMEN)
        self.wait_for_element_appear(*self.NEW_MEN)
        self.wait_for_element_appear(*self.NEW_GIRLS)
        self.wait_for_element_appear(*self.NEW_BOYS)
        self.wait_for_element_appear(*self.NEW_BABY)
        self.wait_for_element_appear(*self.NEW_LUGGAGE)