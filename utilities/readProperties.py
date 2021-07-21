import configparser

#config is object
config = configparser.RawConfigParser()
config.read("/Users/toad/Documents/My_Projects/nopCommerceApp_selenium_python_pytest/Configurations/config.ini")

class ReadConfig:
    #method can be accessed directly by class name without creating object
    @staticmethod
    def getApplicationURL():
        url = config.get('common info', 'baseURL')
        return url

    @staticmethod
    def getUseremail():
        username = config.get('common info', 'username')
        return username

    @staticmethod
    def getPassword():
        password = config.get('common info', 'password')
        return password

    @staticmethod
    def getbrowser():
        browser = config.get('common info', 'browser')
        return browser

    @staticmethod
    def getdriverpath():
        chromedriverpath = config.get('common info', 'chromeDriverPath')
        return chromedriverpath





