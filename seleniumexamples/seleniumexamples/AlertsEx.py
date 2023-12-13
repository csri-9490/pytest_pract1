import time

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
# from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome()

driver.get("https://mail.rediff.com/cgi-bin/login.cgi")
driver.maximize_window()
driver.implicitly_wait(1)

driver.find_element(By.XPATH,"//input[@name='proceed']").click()

alert = driver.switch_to.alert

print(alert.text)
time.sleep(3)
alert.accept()