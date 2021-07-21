from selenium import webdriver
import pytest
from webdriver_manager.chrome import ChromeDriverManager
from utilities.readProperties import ReadConfig


@pytest.fixture()
def setup():
    browser = ReadConfig.getbrowser()
    chromedriverpath = ReadConfig.getdriverpath()
    print("browser name - " +browser)
    #driver = webdriver.Chrome()
    if browser == 'chrome':
        driver = webdriver.Chrome(executable_path = chromedriverpath)
    elif browser == 'firefox':
        driver = webdriver.Firefox()
    elif browser == 'IE':
        driver = webdriver.Ie()
    else:
        driver = webdriver.Chrome(executable_path="C:\\Users\\agovindara21\\Downloads\\chromedriver1\\chromedriver.exe")
    return driver

######Pytest HTML Report ##########

#hook for adding envt info to HTML Report
def pytest_configure(config):
    config._metadata['Project Name'] = 'nop Commerce'
    config._metadata['Modular Name'] = 'Customers'
    config._metadata['Tester'] = 'Anu'

#hook to delete/modify envt info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)







#hook to delete/ modify envt info to HTML Report

