import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from pageObjects.LoginPage import LoginPage
from utiliteis.ReadPropreties import read_config
from utiliteis.customLogger import LogGen
from testCases.test_Login import Test_001_Login
from pageObjects.AddAccountPage import addAccount


class Test_004_AddAccount:

    def test_add_account(self, setup):
        self.driver = setup
        self.logger = LogGen.loggen()
        self.logger.info("Logger initialized.")
        self.logger.info("*****************Test_004_AddAccount******************")
        self.logger.info("*****************verifying adding a new account****************")

        # Navigate to the login page
        self.driver.get(Test_001_Login.base_url)
        time.sleep(2)  # Wait for the page to load

        # Log in
        self.lp = LoginPage(self.driver)
        self.lp.setUsername(Test_001_Login.username)
        time.sleep(1)  # Wait for 1 second before entering the password
        self.lp.setPassword(Test_001_Login.password)
        time.sleep(1)  # Wait for 1 second before clicking the login button
        self.lp.clickLoginButton()
        time.sleep(2)  # Wait for the dashboard or home page to load

        self.driver.maximize_window()

        # Initialize the AddAccount page
        self.add_account = addAccount(self.driver)
        time.sleep(1)  # Short wait before performing the next action

        # Add a new account
        self.add_account.add_account("shenn", "saving", "20000", "176885789876", "12999go@gmail.com")
        time.sleep(2)  # Wait for the account to be added (adjust as necessary)

        # Verify the account was added
        data = self.driver.find_element(By.XPATH,"//*[@id='DataTables']/tbody").text
        print(data)

        if "shenn" in data and "12999go@gmail.com" in data:
            self.logger.info("Account added successfully")
            assert True, "Test Case Passed: Account added successfully"
        else:
            self.driver.save_screenshot('./Screenshots/AccountNotAdded.png')
            self.logger.info("************ test fail******************")
            assert False, "Test Case Failed: Account not added"




