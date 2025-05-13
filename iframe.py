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
# driver.get("https://the-internet.herokuapp.com/iframe")
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

driver.switch_to.frame("courses-iframe")
driver.find_element(By.LINK_TEXT,"VIEW ALL COURSES").click()
# driver.find_element(By.ID,"tinymce").send_keys("Automating iFrames")
time.sleep(3)
driver.switch_to.default_content()

driver.find_element(By.ID,"autocomplete").send_keys("Automating iFrames")

time.sleep(5)
