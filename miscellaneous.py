import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

# ------------- Run in Headless Mode -----------------------
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("headless")
# -------------------------------------------------------------

chrome_options.add_argument("--ignore-certificate-errors")

driver = webdriver.Chrome(options=chrome_options)
# Global Time out - max 5 seconds
driver.implicitly_wait(5)   #Applying Implicit Wait
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
driver.get_screenshot_as_file("screen.png")

time.sleep(3)