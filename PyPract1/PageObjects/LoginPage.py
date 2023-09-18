import pytest
from selenium.webdriver.common.by import By

from testCases.conftest import logins
import time


# @pytest.mark.usefixtures("logins")
from utilities.readProperties import ReadConfig


class loginPage:
    textbox_signin_xpath="//*[contains(text(),'Sign In')]"
    textbox_uname_css="#email"
    textbox_pwd_xpath="//input[@name='login[password]']"
    button_signin_xpath="//fieldset[@class='fieldset login']//span[contains(text(),'Sign In')]"

    def __init__(self,driver):
        self.driver=driver

    def siginbutton(self):
        self.driver.find_element(By.XPATH,self.textbox_signin_xpath).click()


    def username(self,uname):
        time.sleep(5)
        self.driver.find_element(By.CSS_SELECTOR,self.textbox_uname_css).send_keys(uname)


    def setpwd(self,pwd):
        time.sleep(5)
        self.driver.find_element(By.XPATH,self.textbox_pwd_xpath).send_keys(pwd)

    def clicklogin(self):
        self.driver.find_element(By.XPATH,self.button_signin_xpath).click()


