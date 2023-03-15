from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

TOP_MENU_OPTIONS = (By.CSS_SELECTOR, "#zg_header li a")
SELECTED_TOP_MENU = (By.CSS_SELECTOR, "#zg_banner_text")


@then('Verify correct page open, close and back to page')
def click_top_menu_loop(context):
    context.all_top_menu_options = context.driver.find_elements(*TOP_MENU_OPTIONS)
    print(context.all_top_menu_options)

    for i in range(len(context.all_top_menu_options)):
        linked_top_menu = context.driver.find_elements(*TOP_MENU_OPTIONS)[i]
        link_top_title = linked_top_menu.text
        print("link_top_title :", link_top_title)
        linked_top_menu.click()
        linked_title = context.driver.find_element(*SELECTED_TOP_MENU).text
        print("linked_title :", linked_title)
        assert link_top_title in linked_title, "NOT correct link"
