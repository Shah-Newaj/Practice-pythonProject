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
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

action = ActionChains(driver)
# action.scroll_to_element(driver.find_element(By.ID,"mousehover")).perform()
action.move_to_element(driver.find_element(By.ID,"mousehover")).perform()
action.context_click(driver.find_element(By.XPATH,"//div[@class='mouse-hover']/div/a[2]")).perform()


time.sleep(5)