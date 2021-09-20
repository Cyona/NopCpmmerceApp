from selenium import webdriver
import pytest
from pageObjects.LoginPage import Login
from utilities.readproperties import ReadConfig
from utilities.customLogger import LogGen
class Test_001_login:
    base_url = ReadConfig.getBaseUrl()
    user = ReadConfig.getusername()
    password = ReadConfig.getPassword()

    logger=LogGen.logGen()

    @pytest.mark.regression
    def test_homePageTitle(self,setup):
        self.logger.info("******* Test_001_login **********")
        self.logger.info("******* verifying home page title ********")
        self.driver = setup
        self.driver.get(self.base_url)
        act_title = self.driver.title
        if act_title == 'You store. Login':
            assert True
            self.driver.close()
            self.logger.info("******* home page title test is passed********")

        else:
            self.driver.save_screenshot(".\\screenshots\\"+"title.png")
            self.driver.close()
            self.logger.error("*******  home page title test is failed ********")

            assert False

    @pytest.mark.regression
    @pytest.mark.sanity
    def test_login(self,setup):
        self.logger.info("******* verifying login test ********")

        self.driver = setup
        self.driver.get(self.base_url)
        lp = Login(self.driver)
        lp.setUsername(self.user)
        lp.setPassword(self.password)
        lp.clickLogin()
        act_title = self.driver.title
        print(act_title)
        self.logger.info("******* Login test success ********")
        self.driver.close()
