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
    def test_searchCustomerByEmail(self, setup):
        self.logger.info("************* SearchCustomerByEmail_004 **********")
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

        self.logger.info("************* searching customer by emailID **********")
        searchcust = SearchCustomer(self.driver)
        searchcust.setEmail("victoria_victoria@nopCommerce.com")
        searchcust.clickSearch()
        time.sleep(5)
        status = searchcust.searchCustomerByEmail("victoria_victoria@nopCommerce.com")
        #print(searchcust.emailid)
        assert True == status
        self.driver.close()
        self.logger.info("***************  TC_SearchCustomerByEmail_004 Finished  *********** ")
