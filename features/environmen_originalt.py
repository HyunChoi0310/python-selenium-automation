from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.events import EventFiringWebDriver

from app.application import Application
from support.logger import logger, MyListener


def browser_init(context):
    # context.driver = webdriver.Safari()
    #service = Service("C:/Users/thoma/PycharmProjects/python-selenium-automation/geckodriver.exe")
    # context.driver = webdriver.Firefox(service=service)
    service = Service("C:/Users/thoma/PycharmProjects/python-selenium-automation/chromedriver.exe")
    context.driver = webdriver.Chrome(service=service)
# #  context.driver = webdriver.Chrome(executable_path="/chromedriver.exe")
    # context.browser = webdriver.Safari()
    # context.browser = webdriver.Firefox()
    # options = webdriver.ChromeOptions()
    # options.add_argument('headless')
    # context.driver = webdriver.Chrome(chrome_options = options,
    #                                     service=service)

    ### EventFiringWebDriver - log file ###
    ### for drivers ###
    context.driver = EventFiringWebDriver(
        webdriver.Chrome(service=service),
        MyListener()
    )

    context.driver.maximize_window()
    context.driver.implicitly_wait(4)
    context.driver.wait = WebDriverWait(context.driver, 10)
    context.app = Application(driver=context.driver)

    context.app = Application(context.driver)


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context)
    # print('\nStarted scenario: ', scenario.name)
    logger.info(f'Started scenario: {scenario.name}')
    browser_init(context, scenario.name)


def before_step(context, step):
    print('\nStarted step: ', step)
    # print('\nStarted step: ', step)
    logger.info(f'Started step: {step}')


def after_step(context, step):
    if step.status == 'failed':
        logger.error(f'Step failed: {step}')
        print('\nStep failed: ', step)
        # Mark test case as FAILED on BrowserStack:
        # context.driver.execute_script(
        #     'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "Step failed"}}')


def after_scenario(context, feature):
    context.driver.delete_all_cookies()
    context.driver.quit()
