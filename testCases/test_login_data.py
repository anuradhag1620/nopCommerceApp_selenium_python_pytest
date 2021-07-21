# Implement testcase for the Page object class

import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from utilities import XLUtils

# package, filename import classname

from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

# Class name is test case ID. Access class by using self keyword
# create and object of login page, constructor expects driver as parameter
class Test_002_Login:

    baseURL = ReadConfig.getApplicationURL()
    path = ".//TestData//LoginData.xlsx"

    # returns logger object
    logger = LogGen.loggen()

    def test_login_ddt(self, setup):


        #XL util
        self.rows = XLUtils.getRowCount(self.path,'Sheet1')
        print("Number of rows", self.rows)

        for r in range(2,self.rows+1):
            self.logger.info("***********Verifying login test***********")
            self.driver = setup
            self.driver.get(self.baseURL)
            self.lp = LoginPage(self.driver)
            self.username=XLUtils.readData(self.path,'Sheet1',r,1)
            self.password = XLUtils.readData(self.path, 'Sheet1', r, 2)
            self.lp.setUserName(self.username)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            act_title = self.driver.title
            print(act_title)

            if act_title == "Dashboard / nopCommerce administration":
                self.lp.clickLogout()
                assert True
                self.logger.info("Login test passed")
            else:
                self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")
                self.logger.error("Login test failed")

