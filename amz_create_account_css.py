from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
# init driver
service = Service("C:/Users/thoma/PycharmProjects/python-selenium-automation/chromedriver.exe")
driver = webdriver.Chrome(service=service)
#driver = webdriver.Chrome(executable_path="C:/Users/thoma/PycharmProjects/python-selenium-automation/chromedriver.exe")
driver.maximize_window()
# open the url
driver.get('https://www.amazon.com/')

#By CSS, using class : amazon logo
driver.find_element(By.CSS_SELECTOR, "i.a-icon.a-icon-logo")

#By CSS, using class : Create account
driver.find_element(By.CSS_SELECTOR, "h1.a-spacing-small")

#By CSS, using class : name field
driver.find_element(By.CSS_SELECTOR, "input.a-input-text.a-span12.auth-autofocus.auth-required-field")

#By CSS, using class : email field
driver.find_element(By.CSS_SELECTOR, "input.a-input-text.a-span12.a-spacing-micro.auth-required-field")

#By CSS, using class : password field
driver.find_element(By.CSS_SELECTOR, "input.a-input-text.a-span12.auth-required-field.auth-require-fields-match.auth-require-password-validation")

#By CSS, using ID : re_password field
driver.find_element(By.CSS_SELECTOR, "input#ap_password_check")

#By CSS, using class : continue button
driver.find_element(By.CSS_SELECTOR, "input.a-button-input")

#By CSS, using ID, class, parent to child : Condition of USE link(??)
driver.find_element(By.CSS_SELECTOR, "div.a-section.a-spacing-extra-large #legalTextRow a[href*=condition_of_use]")

#By CSS, using ID, class, parent to child : Privacy Notice link(??)
driver.find_element(By.CSS_SELECTOR, "div.a-section.a-spacing-extra-large #legalTextRow a[href*=privacy_notice]")

#By CSS, using class, parent to child : Sign In link(??)
driver.find_element(By.CSS_SELECTOR, "div.a-row a[href*=sign_in]")