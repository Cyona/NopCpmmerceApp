from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By


class Login:
    def __init__(self,driver):
        self.driver=driver

    username=(By.ID,"Email")
    password="Password"
    login=(By.XPATH,"//button[@class='button-1 login-button']")
    logout=(By.LINK_TEXT,"Logout")

    def setUsername(self,name):
        self.driver.find_element(*Login.username).clear()
        self.driver.find_element(*Login.username).send_keys(name)
    def setPassword(self,passwd):
        self.driver.find_element_by_id(self.password).clear()
        self.driver.find_element_by_id(self.password).send_keys(passwd)
    def clickLogin(self):
        self.driver.find_element(*Login.login).click()
    def clickLogout(self):
        self.driver.find_element(*Login.logout).click()


