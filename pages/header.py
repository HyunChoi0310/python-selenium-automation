from selenium.webdriver.common.by import By
from pages.base_page import Page
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select

class Header(Page):
    AMAZON_SEARCH_FIELD = (By.ID, 'twotabsearchtextbox')
    SEARCH_ICON = (By.ID, 'nav-search-submit-button')
    LANG_OPTIONS = (By.CSS_SELECTOR, '.icp-nav-link-inner')
    SPANISH_LANG = (By.CSS_SELECTOR, 'a[href="#switch-lang=es_US"]')
    SELECT_DEPARTMENT = (By.CSS_SELECTOR, '#searchDropdownBox')
    NEW_ARRIVALS = (By.CSS_SELECTOR, '.nav-a.nav-hasArrow[aria-label="New Arrivals"]')

    def input_search_text(self, text):
        self.input_text(text, *self.AMAZON_SEARCH_FIELD)

    def click_search(self):
        self.click(*self.SEARCH_ICON)

    def hover_lang_options(self):
        lang_options = self.find_element(*self.LANG_OPTIONS)
        actions = ActionChains(self.driver)
        actions.move_to_element(lang_options)
        actions.perform()

    def hover_new_arrival(self):
        new_arrivals = self.find_element(*self.NEW_ARRIVALS)
        actions = ActionChains(self.driver)
        actions.move_to_element(new_arrivals)
        actions.perform()

    def select_department(self, alias):
        select_dd = self.driver.find_element(*self.SELECT_DEPARTMENT)
        select = Select(select_dd)
        select.select_by_value(f'search-alias={alias}')

    def verify_lang_shown(self):
        self.wait_for_element_appear(*self.SPANISH_LANG)

