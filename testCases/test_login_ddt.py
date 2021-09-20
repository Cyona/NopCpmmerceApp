from selenium import webdriver
from utilities import ExcelUtils
import pytest
from pageObjects.LoginPage import Login
from utilities.readproperties import ReadConfig
from utilities.customLogger import LogGen
class Test_DDT_002_login:
    base_url = ReadConfig.getBaseUrl()
    path="./testdata/LoginData.xlsx"
    logger=LogGen.logGen()
    print(path)

    @pytest.mark.regression
    def test_login_ddt(self,setup):

        self.logger.info("****** test_login_ddt *********")
        self.logger.info("******* verifying login test ********")

        self.driver = setup
        self.driver.get(self.base_url)
        lp = Login(self.driver)

        self.rows=ExcelUtils.getRowCount(self.path,"Sheet1")
        print("Number of rows in excel",self.rows)

        list_status=[]  #empty list

        for r in range(2,self.rows+1):
            self.user=ExcelUtils.readData(self.path,'Sheet1',r,1)
            self.password = ExcelUtils.readData(self.path, 'Sheet1', r, 2)
            self.exp = ExcelUtils.readData(self.path, 'Sheet1', r, 3)


            lp.setUsername(self.user)
            lp.setPassword(self.password)
            lp.clickLogin()
            act_title = self.driver.title
            exp_title= "Dashboard / nopCommerce administration"
            if act_title==exp_title:
                if self.exp== "Pass":
                    self.logger.info("++++++ Passed ++++++")
                    lp.clickLogout()
                    list_status.append("Pass")
                if self.exp=="Fail":
                    lp.clickLogout()
                    list_status.append("Fail")
                    self.logger.info("+++++++ Failed ++++++")
            elif act_title != exp_title:
                if self.exp == 'Pass':
                    self.logger.info("**** failed ****")
                    list_status.append("Fail")
                elif self.exp == 'Fail':
                    self.logger.info("**** passed ****")
                    list_status.append("Pass")
                print(list_status)
        if 'Fail' not in list_status:
            self.logger.info("**** test_login_ddt passed ****")
            self.driver.close()
            assert True
        else:
            self.logger.info("**** test_login_ddt failed ****")
            self.driver.close()
            assert False
        self.logger.info("******* End of Login DDT Test **********")
        self.logger.info("**************** Completed  TC_LoginDDT_002 ************* ")




