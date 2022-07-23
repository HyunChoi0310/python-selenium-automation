from selenium import webdriver
from selenium.webdriver.common.by import By
# init driver
driver = webdriver.Chrome(executable_path="C:/ChoiLearning/Automation/python-selenium-automation/chromedriver.exe")
driver.maximize_window()
# open the url
driver.get('https://www.amazon.com/')

# Sign in Sign up page
driver.find_element(By.CSS_SELECTOR, "#nav-orders").click()
expected_title = 'Sign-In'
# Expected & Actual
actual_title = driver.find_element(By.CSS_SELECTOR, "h1.a-spacing-small").text
assert actual_title == expected_title, f'Expected {expected_title} but got{actual_title}'

#email is present
assert driver.find_element(By.CSS_SELECTOR, "#ap_email").is_displayed()


driver.quit();