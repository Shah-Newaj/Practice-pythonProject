import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()

# Global Time out - max 5 seconds
driver.implicitly_wait(2)   #Applying Implicit Wait

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.maximize_window()

driver.find_element(By.CSS_SELECTOR,".search-keyword").send_keys("ber")
time.sleep(3)
results = driver.find_elements(By.XPATH,"//div[@class='products']/div/h4") #List
# print(len(results))

expectedList = ['Cucumber - 1 Kg', 'Raspberry - 1/4 Kg', 'Strawberry - 1/4 Kg']
actualList = driver.find_elements(By.XPATH,"//div[@class='products']/div/h4")

for result in results:
    actualList = (result.find_elements(By.XPATH,"//div[@class='products']/div/h4"))

print(actualList)

# assert expectedList == actualList