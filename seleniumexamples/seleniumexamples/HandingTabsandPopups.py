import time

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By

#******* For details in new window after click on current window *******#
driver=webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
driver.implicitly_wait(1)
# windows = driver.window_handles
# for window in windows:
#     print(window)
driver.find_element(By.XPATH,"//button[@id='openwindow']").click()
# windows = driver.window_handles
# for window in windows:
#     print(window)
#     driver.switch_to.window(window)
driver.switch_to.window(driver.window_handles[1])
msg=driver.find_element(By.XPATH,"//div[@class='header-contact text-lg-left text-center']/ul/li[1]/span").text
print(msg)

#******* For details in next tab after click on current tab *******#
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.find_element(By.XPATH,"//a[@id='opentab']").click()
driver.switch_to.window(driver.window_handles[1])
time.sleep(5)
mail_dtls=driver.find_element(By.XPATH,"//div[@class='support float-left']/div[2][@class='cont']/span[1]").text
print(mail_dtls)
driver.quit()