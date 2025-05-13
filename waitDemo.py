import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()

# Global Time out - max 5 seconds
driver.implicitly_wait(2)   #Applying Implicit Wait

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.maximize_window()

driver.find_element(By.CSS_SELECTOR,".search-keyword").send_keys("ber")
time.sleep(3)
results = driver.find_elements(By.XPATH,"//div[@class='products']/div") #List
# print(len(results))

for result in results:
    result.find_element(By.XPATH,"div/button").click()

wait = WebDriverWait(driver,10)     #initializing Explicit wait
driver.find_element(By.CLASS_NAME,"cart-icon").click()
driver.find_element(By.XPATH,"//button[text()='PROCEED TO CHECKOUT']").click()

#Sum Validation
prices = driver.find_elements(By.XPATH,"//tr/td[5]/p")
sum = 0
for price in prices:
    sum = sum + int(price.text)

print("Sum is:", sum)

totalamount = driver.find_element(By.CLASS_NAME,"totAmt").text
print("Total Amount is:", totalamount)

assert sum == int(totalamount)

wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR,".promoCode")))     #Applying Explicit Wait
# wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME,"promoBtn")))
driver.find_element(By.CSS_SELECTOR,".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CLASS_NAME,"promoBtn").click()

wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME,"promoInfo")))    #Applying Explicit Wait
print(driver.find_element(By.CLASS_NAME,"promoInfo").text)

discountamount = driver.find_element(By.CSS_SELECTOR,".discountAmt").text

print("Discount Amount is:", discountamount)
assert totalamount > discountamount

time.sleep(5)