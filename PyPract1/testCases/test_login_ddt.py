
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
import pytest
from selenium.webdriver.common.by import By
from PageObjects.LoginPage_ddt import loginPage_ddt
from PageObjects.LogoutPage import LogoutPage
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig
from utilities import XLUtils


@pytest.mark.usefixtures("logins")
class Test_002_DDT_Login:
    baseURL=ReadConfig.getApplicationURL()
    path="C:\\Users\\srika\\PycharmProjects\\PyPract1\\TestData\\lgndts.xlsx"

    logger=LogGen.loggen()

    def test_homePageTitle(self,setup):
        # self.driver=webdriver.Chrome()
        self.logger.info("******Test_001_login")
        self.driver=setup
        self.driver.get(self.baseURL)
        act_title=self.driver.title
        if act_title=="Home Page":
            assert True
        else:
            self.driver.save_screenshot("C:\\Users\\srika\\PycharmProjects\\PyPract1\\Screenshots\\"+"test_hmpgtitle.png")
            self.driver.close()
            assert False
    def test_login(self,setup,logins):
        # self.driver = webdriver.Chrome()
        self.driver=setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        print('title name',self.driver.title)
        self.lp=loginPage_ddt(self.driver)
        self.lp.siginbutton()
        self.rows=XLUtils.getRowCount(self.path,'Sheet1')
        print("NUmber of rows i a Excel:",self.rows)
        lst_status=[]
        for r in range(2,self.rows+1):
            self.lp.siginbutton()
            self.user=XLUtils.readData(self.path,'Sheet1',r,1)
            self.password=XLUtils.readData(self.path,'Sheet1',r,2)
            # self.exp=XLUtils.readData(self.path,'Sheet1',r,3)
            self.lp.username(self.user)
            self.lp.setpwd(self.password)
            self.lp.clicklogin()
            time.sleep(5)
            self.lgp=LogoutPage(self.driver)
            self.lgp.logoutlink()
            self.lgp.clicklogout()
            time.sleep(5)




