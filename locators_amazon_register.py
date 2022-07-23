from selenium import webdriver
from selenium.webdriver.common.by import By
# init driver
driver = webdriver.Chrome(executable_path="C:/ChoiLearning/Automation/python-selenium-automation/chromedriver.exe")
driver.maximize_window()
# open the url
driver.get('https://www.amazon.com/')
# Amazon logo, By ID
driver.find_element(By.CSS_SELECTOR, " ")
# email field, By ID
driver.find_element(By.ID, "//input[@id='ap_email']")
# Continue button By ID
driver.find_element(By.ID, "//input[@id='continue']")
# Need help link
driver.find_element(By.LINK_TEXT, "//span[contains(text(), 'Need help?')]")
# Create your Amazon account button, By ID
driver.find_element(By.ID, "//a[@id='createAccountSubmit']")
# *Conditions of use link By XPATH
driver.find_element(By.XPATH, "//a[@href='/gp/help/customer/display.html/ref=ap_desktop_footer_cou?ie=UTF8&nodeId=508088']")
# *Privacy Notice link By XPATH
driver.find_element(By.XPATH, "//a[@href='/gp/help/customer/display.html/ref=ap_desktop_footer_privacy_notice?ie=UTF8&nodeId=468496']")

print('Test Passed')
driver.quit()

