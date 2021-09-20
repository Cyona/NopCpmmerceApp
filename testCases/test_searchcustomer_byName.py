import time

import pytest

from pageObjects.AddCustomerPage import AddCustomer
from pageObjects.LoginPage import Login
from pageObjects.SearchCustomerPage import SearchCustomer
from utilities.customLogger import LogGen
from utilities.readproperties import ReadConfig


class Test_SearchCustomerByEmail_004:
    base_url = ReadConfig.getBaseUrl()
    user = ReadConfig.getusername()
    password = ReadConfig.getPassword()
    logger = LogGen.logGen()

    @pytest.mark.regression
    def test_searchCustomerByName(self, setup):
        self.logger.info("************* SearchCustomerByName_005 **********")
        self.driver = setup
        self.driver.get(self.base_url)
        lp = Login(self.driver)
        lp.setUsername(self.user)
        lp.setPassword(self.password)
        lp.clickLogin()
        self.logger.info("++++ login success +++++++")

        addcust = AddCustomer(self.driver)
        addcust.clickOnCustomersMenu()
        addcust.clickOnCustomersMenuItem()

        self.logger.info("************* searching customer by name **********")
        searchcust = SearchCustomer(self.driver)
        searchcust.setFirstName("John")
        searchcust.setLastName("Smith")
        searchcust.clickSearch()
        time.sleep(5)
        status = searchcust.searchCustomerByName("John Smith")
        assert True == status
        self.driver.close()
        self.logger.info("***************  TC_SearchCustomerByName_005 Finished  *********** ")
