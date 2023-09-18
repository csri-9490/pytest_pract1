from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
import time

class CustomUtilities:

   def sleepTime(time1):
       time.sleep(time1)

   def wait_statments(self,time):
      self.driver.implicitly_wait(time)

   def verifyLinkPresence(self,text):
       ele=WebDriverWait(self.driver,10).until(expected_conditions.presence_of_element_located((By.LINK_TEXT,text)))

   def selectOptionByText(self,locator,text):
       sel=Select(locator)
       sel.select_by_visible_text(text)



