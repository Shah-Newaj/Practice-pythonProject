import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()

driver.find_element(By.NAME, "email").send_keys("123@gm.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("1213456")
driver.find_element(By.ID,"exampleCheck1").click()

# XPATH =  //tagname[@attribute = 'value'] -> //input[@type = 'submit']
# CSS_SELECTOR = tagname[attribute = 'value'] -> input[name = 'name'],  #id, .classname
driver.find_element(By.CSS_SELECTOR,"input[name = 'name']").send_keys("Shah Newaj")
driver.find_element(By.CSS_SELECTOR,"#inlineRadio1")
driver.find_element(By.XPATH,"(//input[@type='text'])[3]").send_keys("hello again")
driver.find_element(By.XPATH,"(//input[@type='text'])[3]").clear()

# Static Dropdwon
dropdown = Select(driver.find_element(By.ID,"exampleFormControlSelect1"))
dropdown.select_by_visible_text("Female")
time.sleep(2)
dropdown.select_by_index(0)


driver.find_element(By.XPATH, "//input[@type = 'submit']").click()
message = driver.find_element(By.CLASS_NAME, 'alert-success').text
print(message)
assert "Success" in message



time.sleep(5)