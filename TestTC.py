from selenium import webdriver
from selenium.webdriver.common.by import By
# init driver
driver = webdriver.Chrome(executable_path="//chromedriver.exe")
driver.maximize_window()
# open the url
driver.get('www.amazon.com')
# Expected & Actual
ExpectedTitle = "Amazon Sign-In"
ActualTitle = driver.getTitle()
# Sign in Sign up page
driver.find_element(By.LINK_TEXT, "//h2[text()='Your Account']").click()
driver.find_element(By.LINK_TEXT, "//h2[text()='Your Orders']").click()

assert ActualTitle == ExpectedTitle, f'Expected {ExpectedTitle} but got{ActualTitle}'
print("Verified for Signing in")

email_p = driver.findElement(By.xpath("//input[@type='ap_email']")).isEnabled
if email_p:
print('Email is present')

driver.close();
driver.quit();