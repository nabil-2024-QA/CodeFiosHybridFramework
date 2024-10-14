import time
import random
import string
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from pageObjects.LoginPage import LoginPage
from utiliteis.ReadPropreties import read_config
from utiliteis.customLogger import LogGen
from pageObjects.AddCustomerPage import AddCustomer

class Test_003_AddCustomer:
    base_url = read_config.get_base_url()
    username = read_config.get_username()
    password = read_config.get_password()
    logger = LogGen.loggen()
    logger.info("Logger initialized.")
    @pytest.mark.regression
    def test_addCustomer(self, setup):
        self.logger.info("*****************Test_003_AddCustomer******************")
        self.logger.info("*****************verifying login with valid credentials****************")
        self.driver = setup
        self.driver.get(self.base_url)
        self.driver.maximize_window()
        time.sleep(2)  # Wait 2 seconds

        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.username)
        time.sleep(2)  # Wait 2 seconds
        self.lp.setPassword(self.password)
        time.sleep(2)  # Wait 2 seconds
        self.lp.clickLoginButton()
        time.sleep(2)  # Wait 2 seconds

        expected_title = "Codefios"
        actual_title = self.driver.title
        if expected_title == actual_title:
            self.logger.info("Login Successful")
            assert True, "Test Case Passed: Login Successful"
        else:
            self.driver.save_screenshot('./Screenshots/LoginFailed.png')
            self.logger.info("************ test fail******************")
            assert False, "Test Case Failed: Login Failed"

        self.addcust = AddCustomer(self.driver)

        self.addcust.clickCustomersLink()
        time.sleep(2)  # Wait 2 seconds

        self.addcust.clickAddCustomerLink()
        time.sleep(2)

        expected_title = "Manage Client"
        actual_title = self.driver.title
        if expected_title == actual_title:
            self.logger.info("Add Customer Page Title is Correct")
            assert True, "Test Case Passed: Add Customer Page Title is Correct"
        else:
            self.driver.save_screenshot('./Screenshots/AddCustomerPageTitleMismatch.png')
            self.logger.info("************ test fail******************")
            assert False, "Test Case Failed: Add Customer Page Title is Incorrect"

        self.addcust.addCompany()
        time.sleep(2)  # Wait 2 seconds

        self.addcust.enterCompanyName("Metro")
        time.sleep(2)  # Wait 2 seconds

        self.addcust.enterURL("www.metro.com")
        time.sleep(2)  # Wait 2 seconds

        self.addcust.enterCompanyEmail("capmtero@gmail.com")
        time.sleep(2)  # Wait 2 seconds

        self.addcust.enterCompanyPhone("1234567890")
        time.sleep(2)  # Wait 2 seconds

        self.addcust.enterLogoUrl("cap metro")
        time.sleep(2)  # Wait 2 seconds

        self.addcust.clickNewCompanyButton()
        time.sleep(6)  # Wait 2 seconds

        self.addcust.enterFullName("sakouchi yokama")
        time.sleep(2)  # Wait 2 seconds

        self.addcust.selectCompany("Metro")
        time.sleep(2)  # Wait 2 seconds

        random_generator = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
        self.email = random_generator + "@gmail.com"

        self.addcust.enterEmail(self.email)
        time.sleep(2)  # Wait 2 seconds

        self.random_digit = random.randint(1000000000, 9999999999)
        print(self.random_digit)

        self.addcust.enterPhone(self.random_digit)
        time.sleep(2)  # Wait 2 seconds

        self.addcust.enterAddress("123 Main St")
        time.sleep(2)  # Wait 2 seconds

        self.addcust.enterCity("Paris")
        time.sleep(2)  # Wait 2 seconds

        self.addcust.enterZipCode("10001")
        time.sleep(2)

        self.addcust.selectCountry("France")
        time.sleep(2)  # Wait 2 seconds


        self.addcust.selectGroup("Selenium")
        time.sleep(2)  # Wait 2 seconds

        self.addcust.clickSaveButton()  # Wait 2 seconds

        elements = self.driver.find_elements(By.XPATH, "//*[@id='DataTables']")
        if elements:  # Check if the list is not empty
            self.msg = [element.text for element in elements]
            if "zigomar benx" in self.msg and self.email in self.msg:
                self.logger.info("Test Case Passed: Customer added successfully")
                assert True, "Test Case Passed: Customer added successfully"
        else:
            self.logger.info("No elements found with the specified XPath.")
            self.driver.save_screenshot('./Screenshots/AddCustomerFailed.png')
            assert False, "Test Case Failed: Customer not added successfully"

        self.driver.close()
        self.driver.quit()
