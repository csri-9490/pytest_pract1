from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
s1=[]
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
# fruits=driver.find_elements(By.XPATH,"//div[@class='products']/div/h4[@class='product-name']")
rslts=driver.find_elements(By.XPATH,"//div[@class='products']/div")
for rst in rslts:
    # print(fname.text)
    # s1.append(fname.text)
    rst.find_element(By.XPATH,"div/button").click()
time.sleep(5)
driver.find_element(By.CSS_SELECTOR,"img[alt='Cart']").click()
driver.find_element(By.XPATH,"//*[contains(text(),'PROCEED TO CHECKOUT')]").click()
prices=driver.find_elements(By.CSS_SELECTOR,"tr td:nth-child(5) p")
sum=0
time.sleep(5)
for price in prices:
    sum = sum + int(price.text)
    print('price list',price.text)
print('sum value',sum)
total_amount=int(driver.find_element(By.XPATH,"//span[@class='totAmt']").text)
print('totals',total_amount)
# assert sum==total_amount
time.sleep(5)
driver.find_element(By.XPATH,"//button[contains(text(),'Place Order')]").click()
time.sleep(5)
lsts=Select(driver.find_element(By.XPATH,"//div[@class='products']/div[1]/div[1]/select"))
lsts.select_by_visible_text('India')
time.sleep(5)
driver.find_element(By.CSS_SELECTOR,"input[class='chkAgree']").click()
driver.find_element(By.CSS_SELECTOR,"div[class='wrapperTwo'] button").click()
msg=driver.find_element(By.XPATH,"//span[contains(text(),'Thank you, your order has been placed successfully')]").text
print(msg)