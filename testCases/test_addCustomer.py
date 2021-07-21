import string
from random import random

from pageObjects.AddcustomerPage import AddCustomer
from pageObjects.LoginPage import LoginPage
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig


class Test_003_AddCustomer:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    # setup is for browser
    def test_addCustomer(self, setup):
        self.logger.info("******Test_003_AddCustomer********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info('*******Login successful****')

        self.logger.info('****Add new Customer****')
        self.addcust = AddCustomer(self.driver)

        self.addcust.clickOnCustomersMenu()
        self.addcust.clickOnCustomersMenuItem()
        self.addcust.clickOnAddnew()

        self.logger.info('***Providing new customer info ****')
        #self.email = random_generator() + "@gmail.com"
        self.email = "abc2@gmail.com"
        print(self.email)
        self.addcust.setEmail(self.email)
        self.addcust.setPassword("test123")
        #self.addcust.setCustomerRoles("Guests")
        self.addcust.setManagerOfVendor("Vendor 2")
        self.addcust.setGender("Male")
        self.addcust.setFirstName("Pavan")
        self.addcust.setLastName("Kumar")
        self.addcust.setDob("7/5/1985")
        self.addcust.setCompanyName("busyQA")
        self.addcust.setAdminContent("This is for testing")
        self.addcust.clickOnSave()

        self.logger.info("******Saving customer info****")

        self.logger.info("*****Add Customer validation****")
        self.msg = self.driver.find_element_by_tag_name("body").text
        print(self.msg)
        if 'customer has been added successfully.' in self.msg:
            assert True == True
            self.logger.info("Customer added")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_addCustomer.png")
            self.logger.info("Customer not added")
            assert True == False

        self.driver.close()
        self.logger.info("**Ending Add customer***")


# 8 characters
def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))
