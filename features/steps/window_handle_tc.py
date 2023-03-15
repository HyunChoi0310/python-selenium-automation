from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

#This is working on ONLY 1 window. Can't follow the class. When close the widow, no way to return original window


LINK_PRIVACY_NOTICE = (By.CSS_SELECTOR, "a[href*='/help/customer/display.html?ref_=hp_left_v4_sib&nodeId=GX7NJQ4ZB8MHFRNJ']")
PRIVACY_NOTICE = (By.CSS_SELECTOR, "div.help-service-content h1")
@given('Open Amazon TC page')
def open_tc_page(context):
    context.driver.get('https://www.amazon.com/gp/help/customer/display.html/ref=ap_register_notification_condition_of_use?ie=UTF8&nodeId=508088')
#    context.driver.wait.until(EC.url_contains('https://www.amazon.com/gp/help/customer/display.html/ref=ap_register_notification_condition_of_use?ie=UTF8&nodeId=508088'),
#            message='Amazon Help and Customer Service is NOT open')
#when I use EC, I've got 'Timeout" message.. What is the reason?

@when('Store original windows')
def store_origin_window(context):
    context.origin_window = context.driver.current_window_handle
    print(context.origin_window)


@when('Click on Amazon Privacy Notice link')
def click_pn_link(context):
#    context.driver.wait.until(EC.element_to_be_clickable(LINK_PRIVACY_NOTICE).click())
    context.driver.find_element(*LINK_PRIVACY_NOTICE).click()


@when('Switch to the newly opened window')
def switch_opened_window(context):
    context.driver.wait.until(EC.new_window_is_opened)
    windows = context.driver.window_handles
    print(f'windows :', windows)
    context.current_window = context.driver.current_window_handle
    print(context.current_window)
    context.driver.switch_to.window(context.origin_window)
# window is ONLY one, it changes part of the content(right-center)???

#@then('Verify Amazon Privacy Notice page is opened')
#def verify_pn_page_open(context):
#    context.driver.wait.until(EC.url_contains('https://www.amazon.com/gp/help/customer/'))
#    pn_text = context.driver.find_element(*PRIVACY_NOTICE).text
#    expected_text = "Amazon.com Privacy Notice"
#
#    assert expected_text in pn_text, f'Expected text :, {expected_text} but got {pn_text}'


@then('User can close new window and switch back to original')
def close_new_switch_to_original(context):
    windows = context.driver.window_handles
    print(f'windows :', windows)
    context.driver.close()
    context.driver.switch_to.window(context.origin_window)


#It worked on ONLY 1 window, after close() command, ther is NO window to return???
#Something different to Sign in popup window, I can't figure it out.


