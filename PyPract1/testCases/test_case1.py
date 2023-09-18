from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
import pytest

from selenium.webdriver.common.by import By

# @pytest.mark.usefixtures("logins")
class Test1:
  def test_a11(self,logins):
    driver=webdriver.Chrome(service=Service("D:\\drivers\\chromedriver.exe"))
    # driver.get("https://magento.softwaretestingboard.com/")
# driver.implicitly_wait(10)
# driver.switch_to.new_window("tab")
# driver.get("https://saucelabs.com/resources/blog/automation-frameworks-built-on-top-of-selenium")
# driver.get("https://saucelabs.com/resources/blog/automation-frameworks-built-on-top-of-selenium")
    driver.find_element(By.XPATH,"//*[contains(text(),'Sign In')]").click()
    driver.execute_script("window.scrollBy(0,300)")
    driver.find_element(By.CSS_SELECTOR,"#email").send_keys(logins['uname'])
    time.sleep(5)
    driver.find_element(By.XPATH,"//input[@name='login[password]']").send_keys(logins['pwd'])
    time.sleep(5)
    driver.find_element(By.XPATH,"//fieldset[@class='fieldset login']//span[contains(text(),'Sign In')]").click()
    time.sleep(10)





