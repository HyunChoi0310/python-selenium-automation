from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


DOG_IMAGE = (By.CSS_SELECTOR, 'img#d')


#@given('Open Amazon product B0B8M5FBFQ11111 page')
#def open_404_page(context):
#    context.driver.wait.until(EC.url_contains('https://www.amazon.com/dp/B0B8M5FBFQ11111/ref=va_live_carousel?pf_rd_r=FP58ATZWJN56X3GKWWB1&pf_rd_p=afcd7c04-19b2-43a3-a1f1-e0e6205908e4&pf_rd_m=ATVPDKIKX0DER&pf_rd_t=browse&pf_rd_i=7147440011&pf_rd_s=merchandised-search-2&linkCode=ilv&tag=onamzdevynsim-20&ascsubtag=Fashion_Finds_Sponsored_by_Logitech_230302200131&asc_contentid=amzn1.amazonlive.broadcast.0d89b7a8-9341-4e50-8824-653afbdfb937&pd_rd_i=B0B8M5FBFQ&th=1&psc=1'),
#            message='404 page is NOT open')


@given('Store original window')
def store_current_window(context):
    context.original_window = context.driver.current_window_handle
    print(f'Before_current_window is :', context.original_window)


@when('Click on a dog image')
def click_dog_image(context):
#    context.driver.wait.until(EC.element_to_be_clickable(CLICK_DOG_IMAGE),
#            message='Dog image is NOT clickable').click()
    context.driver.find_element(*DOG_IMAGE).click()

@when('Switch to the new window')
def switch_window(context):
    context.driver.wait.until(EC.new_window_is_opened)
    windows = context.driver.window_handles
    print(f'All windows :' , windows)
    context.driver.switch_to.window(windows[1])
    context.current_window = context.driver.current_window_handle
    print(f'After_current_window is :', context.current_window)


@then('verify blog is opened')
def verify_blog_open(context):
    context.driver.wait.until(EC.url_contains('https://www.aboutamazon.com/news/workplace/how-much-does'))


@then('Close blog')
def close_blog(context):
    context.driver.close()


@then('Return to original window')
def return_original_window(context):
    context.driver.switch_to.window(context.original_window)
    print(f'Original window : ', context.original_window)
