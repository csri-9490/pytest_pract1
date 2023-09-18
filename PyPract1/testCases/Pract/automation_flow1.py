from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
s1=[]
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
time.sleep(5)
driver.find_element(By.XPATH,"//input[@class='search-keyword']").send_keys("ber")
time.sleep(5)
names=driver.find_elements(By.XPATH,"//div[@class='products']/div/h4[@class='product-name']")
for nm in names:
    s1.append(nm.text)
print(s1)
s2=['Cucumber - 1 Kg','Raspberry - 1/4 Kg','Strawberry - 1/4 Kg']
assert  s1==s2
