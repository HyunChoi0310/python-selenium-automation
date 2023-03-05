from selenium import webdriver
from selenium.webdriver.common.by import By
# init driver
driver = webdriver.Chrome(executable_path="C:/Users/thoma/PycharmProjects/python-selenium-automation/chromedriver.exe")
driver.maximize_window()
# open the url
driver.get('https://www.amazon.com/ap/signin?openid.pape.max_auth_age=900&openid.return_to=https%3A%2F%2Fwww.amazon.com%2Fgp%2Fyourstore%2Fhome%3Fpath%3D%252Fgp%252Fyourstore%252Fhome%26signIn%3D1%26useRedirectOnSuccess%3D1%26action%3Dsign-out%26ref_%3Dnav_AccountFlyout_signout&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0')
# Amazon logo, By ID
driver.find_element(By.XPATH, "//a[@href='/ref=ap_frn_logo']")
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
