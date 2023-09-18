from selenium.webdriver.common.by import By
import time


class amzn_loginPage:

    amzn_sigin="//div[@id='nav-signin-tooltip']//span[@class='nav-action-inner'][normalize-space()='Sign in']"
    amzn_username="//input[@id='ap_email']"
    amzn_usrnme_cont="//input[@id='continue']"
    amzn_pwd="//input[@id='ap_password']"
    click_signin="//input[@id='signInSubmit']"
    def __init__(self, driver):
        self.driver = driver

    def username(self,uname):
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH,self.amzn_sigin).click()
        self.driver.find_element(By.XPATH,self.amzn_username).send_keys(uname)
        self.driver.find_element(By.XPATH,self.amzn_usrnme_cont).click()
    def pswrd(self,pwd):
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH,self.amzn_pwd).send_keys(pwd)
    def signin(self):
        self.driver.find_element(By.XPATH,self.click_signin).click()
