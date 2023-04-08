from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.service import Service
from app.application import Application
from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.firefox.options import Options

from support.logger import MyListener, logger
from selenium.webdriver.support.events import EventFiringWebDriver

def browser_init(context):
#def browser_init(context, test_name):
    # Configuration for google chrome
    service = Service("./chromedriver.exe")
    options = Options()
    # options.add_argument('--headless')
    context.driver = webdriver.Chrome(service=service, options=options)

    # # Configuration for firefox
    # options = Options()
    # options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
    # context.driver = webdriver.Firefox(executable_path='.\geckodriver.exe', options=options)


    # bs_user = ''
    # bs_key = ''
    # desired_cap = {
    #     'browserName': 'Chrome',
    #     'bstack:options': {
    #         'os': 'Windows',
    #         'osVersion': '10',
    #         'sessionName': test_name
    #     }
    # }
    # bs_user = 'hyunredcloud_TPBt2u'
    # bs_key = '7jxNseRwHAsznZxPXda4'
    # url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'
    # context.driver = webdriver.Remote(url, desired_capabilities = desired_cap)

    context.driver.maximize_window()
    context.driver.implicitly_wait(4)
    context.driver.wait = WebDriverWait(context.driver, 10)
    context.app = Application(driver=context.driver)

def before_scenario(context, scenario):
#   print('\nStarted scenario: ', scenario.name)
    logger.info(f'Started scenario {scenario.name}')
#    browser_init(context, scenario.name)
    browser_init(context)


def before_step(context, step):
# print('\nStarted step: ', step)
    logger.info(f'Started step: {step}')


def after_step(context, step):
    if step.status == 'failed':
#        print('\nStep failed: ', step)
        logger.info(f'Step failed: {step}')


def after_scenario(context, feature):
    context.driver.delete_all_cookies()
    context.driver.quit()
