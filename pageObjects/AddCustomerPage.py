import time

from selenium.webdriver.support.select import Select


class AddCustomer:

    def __init__(self,driver):
        self.driver=driver


    # Add customer Page
    lnkCustomers_menu_xpath = "//a[@href='#']//p[contains(text(),'Customers')]"
    lnkCustomers_menuitem_xpath = "(//*[contains(text(),'Customers')])[2]"
    btnAddnew_xpath = "//a[@class='btn btn-primary']"

    txtEmail_xpath = "//input[@id='Email']"
    txtPassword_xpath = "//input[@id='Password']"
    txtFirstName_xpath = "//input[@id='FirstName']"
    txtLastName_xpath = "//input[@id='LastName']"
    rdFeMaleGender_id = "Gender_Female"
    txtDob_xpath = "//input[@id='DateOfBirth']"
    txtCompanyName_xpath = "//input[@id='Company']"

    txtcustomerRoles_xpath = "(//div[@class='k-multiselect-wrap k-floatwrap'])[2]" #

    lstitemAdministrators_xpath = "//li[contains(text(),'Administrators')]" #customer roles
    lstitemRegistered_xpath = "//li[contains(text(),'Registered')]"
    lstitemGuests_xpath = "//li[contains(text(),'Guests')]"
    lstitemVendors_xpath = "//li[contains(text(),'Vendors')]"

    drpmgrOfVendor_xpath = "//select[@id='VendorId']"
    txtAdminComment_xpath = "//textarea[@id='AdminComment']"
    btnSave_xpath = "//button[@name='save']"

    def clickOnCustomersMenu(self):
        self.driver.find_element_by_xpath(self.lnkCustomers_menu_xpath).click()
        time.sleep(3)

    def clickOnCustomersMenuItem(self):
        self.element=self.driver.find_element_by_xpath(self.lnkCustomers_menuitem_xpath)
        self.driver.execute_script('arguments[0].click();',self.element)
        time.sleep(3)
    def clickOnAddnew(self):
        self.driver.find_element_by_xpath(self.btnAddnew_xpath).click()

    def setEmail(self,email):
        self.driver.find_element_by_xpath(self.txtEmail_xpath).send_keys(email)

    def setPassword(self,password):
        self.driver.find_element_by_xpath(self.txtPassword_xpath).send_keys(password)

    def setFirstName(self, fname):
        self.driver.find_element_by_xpath(self.txtFirstName_xpath).send_keys(fname)

    def setLastName(self, lname):
        self.driver.find_element_by_xpath(self.txtLastName_xpath).send_keys(lname)

    def setGender(self,gender):
        self.driver.find_element_by_id(self.rdFeMaleGender_id).click()

    def setDob(self, dob):
        self.driver.find_element_by_xpath(self.txtDob_xpath).send_keys(dob)

    def setCompanyName(self, comname):
        self.driver.find_element_by_xpath(self.txtCompanyName_xpath).send_keys(comname)

    def setCustomerRoles(self,role):
        self.driver.find_element_by_xpath(self.txtcustomerRoles_xpath).click()
        time.sleep(3)
        if role=='Registered':
            self.listitem=self.driver.find_element_by_xpath(self.lstitemRegistered_xpath)
        elif role=='Administrators':
            self.listitem=self.driver.find_element_by_xpath(self.lstitemAdministrators_xpath)
        elif role=='Guests':
            time.sleep(3)
            self.driver.find_element_by_xpath("//li[@role='option']//span[@class='k-select']").click()
            self.listitem=self.driver.find_element_by_xpath(self.lstitemGuests_xpath)
        elif role=='Vendors':
            self.listitem=self.driver.find_element_by_xpath(self.lstitemVendors_xpath)
        else:
            self.listitem=self.driver.find_element_by_xpath(self.lstitemGuests_xpath)
        time.sleep(3)
        self.driver.execute_script('arguments[0].click();',self.listitem)

    def setManagerOfVendor(self, value):
        ele=self.driver.find_element_by_xpath(self.drpmgrOfVendor_xpath)
        drp = Select(ele)
        drp.select_by_visible_text(value)

    def AdminComment(self,value):
        self.driver.find_element_by_xpath(self.txtAdminComment_xpath).send_keys(value)


    def clickOnSave(self):
        self.driver.find_element_by_xpath(self.btnSave_xpath).click()