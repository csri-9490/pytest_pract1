import pytest
import time

from selenium.webdriver.common.by import By

from PageObjects.amzn_addcrt import Amzn_addcart
from PageObjects.amzn_hmpage import Amzn_HomePage
from PageObjects.amzn_login import amzn_loginPage
from utilities.readProperties import ReadConfig


class Test_001_amazonlogin():
    baseURL=ReadConfig.getamznappurl()
    username=ReadConfig.getamznusername()
    password=ReadConfig.getamznpassword()

    def test_amznlogin(self,setup):
        self.driver=setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        amzn_lp=amzn_loginPage(self.driver)
        amzn_lp.username(self.username)
        amzn_lp.pswrd(self.password)
        amzn_lp.signin()
        time.sleep(5)
    def test_amznhmpage(self,setup):
        self.driver=setup
        amzn_hp=Amzn_HomePage(self.driver)
        amzn_hp.leftclick()
        amzn_hp.new_releases()
        amzn_hp.page_down()
        amzn_hp.prod_selection()
    def test_amznaddcart(self,setup):
        self.driver=setup
        amzn_addcart=Amzn_addcart(self.driver)
        # print(amzn_addcart.getprice())
        amzn_addcart.getqty()
        amzn_addcart.addcart()
        amzn_addcart.prcdchckout()





