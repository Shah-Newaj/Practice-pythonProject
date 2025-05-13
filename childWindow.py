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
driver.get("https://the-internet.herokuapp.com/windows")
driver.maximize_window()
# driver.find_element(By.XPATH,"//div[@class='example']/a").click()
driver.find_element(By.LINK_TEXT,"Click Here").click()
time.sleep(2)
windowOpened = driver.window_handles
driver.switch_to.window(windowOpened[1])
# print(driver.find_element(By.XPATH,"//div/h3").text)
print(driver.find_element(By.TAG_NAME,"h3").text)
driver.close()

driver.switch_to.window(windowOpened[0])

assert "Opening a new window" == driver.find_element(By.TAG_NAME,"h3").text