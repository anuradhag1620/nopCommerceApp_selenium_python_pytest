# Implement testcase for the Page object class

import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# package, filename import classname

from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


# Class name is test case ID. Access class by using self keyword
# create and object of login page, constructor expects driver as parameter
class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()

    # returns logger object
    logger = LogGen.loggen()

    def test_homePageTitle(self, setup):
        self.logger.info("***********Test_001_Login***********")
        self.logger.info("Verifying home page title")
        self.driver = setup
        self.driver.get(self.baseURL)
        actual_title = self.driver.title

        if actual_title == "Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("Home Page title test is passed")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_homePageTitle.png")
            self.driver.close()
            self.logger.error("Home Page title test is failed")
            assert False

    def test_login(self, setup):
        self.logger.info("***********Verifying login test***********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title
        print(act_title)

        if "Dashboard" in act_title:
            assert True
            self.logger.info("Login test passed")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")
            assert False
            self.driver.close()
            self.logger.error("Login test passed")