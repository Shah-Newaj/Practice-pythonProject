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
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
driver.maximize_window()

# Click on Column Header to sort the items
driver.find_element(By.XPATH,"//span[text()='Veg/fruit name']").click()

# Collect all veggie names
veggieWebElements = driver.find_elements(By.XPATH,"//tr/td[1]")
browserSortedVeggies = [ele.text for ele in veggieWebElements]
print(browserSortedVeggies)

originalBrowserSortedVeggies = browserSortedVeggies.copy()
print(originalBrowserSortedVeggies)

# now sort the browser sorted list
browserSortedVeggies.sort()
assert originalBrowserSortedVeggies == browserSortedVeggies