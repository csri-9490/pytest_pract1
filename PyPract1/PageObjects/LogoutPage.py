from selenium.webdriver.common.by import By


class LogoutPage:
    button_selection_xpath="(//button[@class='action switch'])[1]"
    link_logout_xpath="(//*[contains(text(),'Sign Out')])[1]"

    def __init__(self,driver):
        self.driver=driver

    def logoutlink(self):
        self.driver.find_element(By.XPATH,self.button_selection_xpath).click()

    def  clicklogout(self):
        self.driver.find_element(By.XPATH,self.link_logout_xpath).click()