import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
# Global Time out - max 5 seconds
driver.implicitly_wait(5)   #Applying Implicit Wait
driver.get("https://rahulshettyacademy.com/loginpagePractise/")
driver.maximize_window()

driver.find_element(By.XPATH,"//body/a").click()
windowOpened = driver.window_handles
driver.switch_to.window(windowOpened[1])
email = driver.find_element(By.XPATH,"//div/p[@class='im-para red']/strong").text
driver.close()
driver.switch_to.window(windowOpened[0])

driver.find_element(By.ID,"username").send_keys(email)
driver.find_element(By.ID,"password").send_keys("learning")
driver.find_element(By.ID,"signInBtn").click()

# explicit wait is must here
wait = WebDriverWait(driver,10)
# using XPATH
# wait.until(expected_conditions.visibility_of_element_located((By.XPATH,"//div[@class='alert alert-danger col-md-12']")))
# print(driver.find_element(By.XPATH,"//div[@class='alert alert-danger col-md-12']").text)

# using css selector
wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR,".alert-danger")))
print(driver.find_element(By.CSS_SELECTOR,".alert-danger").text)
