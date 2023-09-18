from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class Amzn_addcart:

    span_price_xpath="//div[@id='corePrice_feature_div']/div[1]/span[1]/span[2]/span[2]"
    select_qtys="//select[@name='quantity']"
    addtcart="//input[@id='add-to-cart-button']"
    prcchckout_xpath="//span[@id='attach-sidesheet-checkout-button']/span"

    def __init__(self,driver):
        self.driver=driver

    def getprice(self):
        price=self.driver.find_element(By.XPATH,self.span_price_xpath).text
        return price

    def getqty(self):
        qts=Select(self.driver.find_element(By.XPATH,self.select_qtys))
        qts.select_by_value('3')
    def addcart(self):
        self.driver.find_element(By.XPATH,self.addtcart).click()
    def prcdchckout(self):
        self.driver.find_element(By.XPATH,self.prcchckout_xpath).click()

