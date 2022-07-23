from selenium import webdriver
from selenium.webdriver.common.by import By
# init driver
driver = webdriver.Chrome(executable_path="C:/ChoiLearning/Automation/python-selenium-automation/chromedriver.exe")
driver.maximize_window()
# open the url
driver.get('https://www.amazon.com/ap/register?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2Fref%3Dap_frn_logo%2F%3F_encoding%3DUTF8%26ref_%3Dnav_newcust&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&')
#logo
driver.find_element(By.CSS_SELECTOR, "i.a-icon.a-icon-logo")
#create account
driver.find_element(By.CSS_SELECTOR, "h1.a-spacing-small")
#your name
driver.find_element(By.CSS_SELECTOR, "input#ap_customer_name")
#your email
driver.find_element(By.CSS_SELECTOR, "ap_email")
#your password
driver.find_element(By.CSS_SELECTOR, "ap_password")
#Passwords must be at least 6 characters.
driver.find_element(By.CSS_SELECTOR, "div.a-alert-content")
#your re-password
driver.find_element(By.CSS_SELECTOR, "ap_password_check")
#continue
driver.find_element(By.CSS_SELECTOR, "input#continue")
#condition of use
driver.find_element(By.CSS_SELECTOR, "a[href='https://www.amazon.com/gp/help/customer/display.html/ref=ap_register_notification_condition_of_use?ie=UTF8&nodeId=508088']")
#notice
driver.find_element(By.CSS_SELECTOR, "https://www.amazon.com/gp/help/customer/display.html/ref=ap_register_notification_privacy_notice?ie=UTF8&nodeId=468496']")
#signin
driver.find_element(By.CSS_SELECTOR, "a-link-emphasis")

print('Test Passed')
driver.quit()