from selenium.webdriver.common.by import By


class Amzn_HomePage:
    a_click_xpath="//div[@id='nav-main']//a[@id='nav-hamburger-menu']"
    a_newrls_xpath="//ul[@class='hmenu hmenu-visible']//a[@class='hmenu-item'][normalize-space()='New Releases']"
    div_prod_xpath="//div[@id='B0C1H6S5X8']//div[@class='p13n-sc-truncate-desktop-type2  p13n-sc-truncated']"
    def __init__(self,driver):
        self.driver=driver
    def leftclick(self):
        self.driver.find_element(By.XPATH,self.a_click_xpath).click()
    def new_releases(self):
        self.driver.find_element(By.XPATH,self.a_newrls_xpath).click()
    def page_down(self):
        self.driver.execute_script("window.scrollBy(0,200)")


    def prod_selection(self):
        self.driver.find_element(By.XPATH,self.div_prod_xpath).click()
