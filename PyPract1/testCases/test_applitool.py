# from PyPract1.utilities.readProperties import ReadConfig
import time
import numpy

import pytest
from selenium.webdriver.common.by import By

from utilities.readProperties import ReadConfig


class TestApplitool:
    burl=ReadConfig.geturl()

    def test_applogins(self,setup):
        s1=[]
        sum=0
        self.driver=setup
        self.driver.get(ReadConfig.getAppURL('applitool','app_url'))
        time.sleep(5)
        # self.driver.get(self.burl)
        self.driver.find_element(By.XPATH,"//input[@id='username']").send_keys("Admin")
        self.driver.find_element(By.XPATH,"//input[@id='password']").send_keys("Password@123")
        self.driver.find_element(By.XPATH,"//a[@id='log-in']").click()
        amounts=self.driver.find_elements(By.XPATH,"//td[@class='text-right bolder nowrap']/span")
        for amount in amounts:
            print(amount.text)
            s1.append(amount.text.split())
        print(s1)
        # print(s1[0][1])
        s2=[]
        # s2.append(s1[0][1])
        s2.append(s1[1][1])
        s2.append(s1[2][1])
        s2.append(s1[3][1])
        s2.append(s1[4][1])
        s2.append(s1[5][1])
        print(s2)
        s3=numpy.array(s2)
        s3=s3.astype(float)
        print(numpy.sum(s3))



