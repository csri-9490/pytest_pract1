
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
import pytest
from selenium.webdriver.common.by import By
from PageObjects.LoginPage import loginPage
from PageObjects.LogoutPage import LogoutPage
from utilities.baseclass import CustomUtilities
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig
from utilities.screenshots import Screenshots


@pytest.mark.usefixtures("logins")
class Test_001_Login(CustomUtilities):
    baseURL=ReadConfig.getApplicationURL()
    username=ReadConfig.getUsername()
    password=""

    logger=LogGen.loggen()

    # @pytest.mark.sanity
    def test_homePageTitle(self,setup):
        # self.driver=webdriver.Chrome()
        self.logger.info("******Test_001_login")
        self.driver=setup
        self.driver.get(self.baseURL)
        scrshots=Screenshots(self.driver)
        act_title=self.driver.title
        if act_title=="Home Page":
            assert True
        else:
            # self.driver.save_screenshot("C:\\Users\\srika\\PycharmProjects\\PyPract1\\Screenshots\\"+"test_hmpgtitle.png")
            scrshots.getscreenshots("C:\\Users\\srika\\PycharmProjects\\PyPract1\\Screenshots\\"+"test_hmpgtitle.png")
            self.driver.close()
            assert False
    # @pytest.mark.smoke
    def test_login(self,setup,logins):
        # self.driver = webdriver.Chrome()
        self.driver=setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        print('title name',self.driver.title)
        self.lp=loginPage(self.driver)
        self.lp.siginbutton()
        # self.driver.find_element(By.XPATH, "//*[contains(text(),'Sign In')]").click()
        # self.lp.username(logins['uname'])
        self.lp.username(self.username)
        self.lp.setpwd(logins['pwd'])
        self.lp.clicklogin()
        # time.sleep(5)
        CustomUtilities.sleepTime(5)
        self.lgp = LogoutPage(self.driver)
        self.lgp.logoutlink()
        self.lgp.clicklogout()
        time.sleep(5)


