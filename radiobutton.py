import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

radiobuttons = driver.find_elements(By.XPATH,"//input[@type='radio']")
print(len(radiobuttons))

driver.find_element(By.XPATH,"//input[@value='radio1']").click()
time.sleep(2)

for radiobutton in radiobuttons:
    if radiobutton.get_attribute("value") == "radio3":
        radiobutton.click()
        assert radiobutton.is_selected()
        break
print(radiobutton.get_attribute("value"))

assert driver.find_element(By.ID,"displayed-text").is_displayed()
driver.find_element(By.ID,"hide-textbox").click()
assert not driver.find_element(By.ID,"displayed-text").is_displayed()


time.sleep(5)