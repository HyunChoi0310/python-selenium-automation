from selenium import webdriver
from selenium.webdriver.common.by import By
# init driver
driver = webdriver.Chrome(executable_path="//chromedriver.exe")
driver.maximize_window()
# open the url
driver.get('')
# Amazon logo, By ID
driver.find_element(By.XPATH, "//a[href='ap_frn_logo']")
# email field, By ID
driver.find_element(By.XPATH, "//input[@label for='ap_email']")
# Continue button By ID
driver.find_element(By.XPATH, "//a[@aria-labelledby='continue-announce']")
# Need help link
driver.find_element(By.LINK_TEXT, "//h2[text()='Need help?']")
# Create your Amazon account button, By ID
driver.find_element(By.ID, "//a[@href='createAccountSubmit']")
# *Conditions of use link By LINK_TEXT
driver.find_element(By.LINK_TEXT, "//h2[text()='Conditions of Use']")
# *Privacy Notice link By LINK_TEXT
driver.find_element(By.LINK_TEXT, "//h2[text()='Privacy Notice']")

print('Test Passed')
driver.quit()

