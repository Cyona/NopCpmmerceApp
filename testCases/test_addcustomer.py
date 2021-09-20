import pytest

from pageObjects.LoginPage import Login
from utilities.customLogger import LogGen
from utilities.readproperties import ReadConfig
from pageObjects.AddCustomerPage import AddCustomer

class Test_AddCustomer:
    base_url = ReadConfig.getBaseUrl()
    user = ReadConfig.getusername()
    password = ReadConfig.getPassword()
    logger=LogGen.logGen()

    @pytest.mark.sanity
    def test_addcustomer(self,setup):
        self.driver=setup
        self.driver.get(self.base_url)
        lp=Login(self.driver)
        lp.setUsername(self.user)
        lp.setPassword(self.password)
        lp.clickLogin()
        self.logger.info("++++ login success +++++++")
        addcust=AddCustomer(self.driver)

        addcust.clickOnCustomersMenu()
        addcust.clickOnCustomersMenuItem()
        addcust.clickOnAddnew()

        addcust.setEmail('samples111@gmail.com')
        addcust.setPassword('Password123#')
        addcust.setFirstName('David')
        addcust.setLastName('Lords')
        addcust.setGender('Female')
        addcust.setDob('04/09/1994')
        addcust.setCompanyName('Dell')
        addcust.setCustomerRoles('Guests')
        addcust.setManagerOfVendor("Vendor 1")
        addcust.AdminComment('This is for testing')
        addcust.clickOnSave()
        self.logger.info("++++ customer added successfully +++++++")


        #self.msg=self.driver.find_element_by_xpath("//div[@class='alert alert-success alert-dismissable']")
        self.msg = self.driver.find_element_by_tag_name("body").text
        if "successful" in self.msg:
            assert True == True
            self.logger.info("******* Test case test_addcustomer passed ******")
        else:
            self.driver.save_screenshot(".\\screenshots\\" + "cust.png")
            self.driver.close()
            self.logger.error('******* Test case test_addcustomer failed ******')
            assert False
        self.driver.close()
        self.logger.info("******* Ending Add customer test **********")