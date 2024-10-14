import pytest
import os
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utiliteis.ReadPropreties import read_config
from utiliteis.customLogger import LogGen


class Test_001_Login:
    base_url = read_config.get_base_url()
    username = read_config.get_username()
    password = read_config.get_password()

    def setup_method(self):
        self.logger = LogGen.loggen()
        self.logger.info("Logger initialized.")

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_homePageTitle(self, setup):
        self.logger.info("*****************Test_001_Login******************")
        self.logger.info("*****************verifying home page title****************")
        self.driver = setup
        self.driver.get(self.base_url)
        expected_title = "Welcome To Codefios"
        actual_title = self.driver.title
        if expected_title == actual_title:
            self.logger.info("Home Page Title is Correct")
            assert True, "Test Case Passed: Home Page Title is Correct"
            self.driver.close()
        else:
            # take a screenshot
            self.driver.save_screenshot('./Screenshots/HomePageTitleMismatch.png')
            assert False, "Test Case Failed: Home Page Title is Incorrect"
            self.logger.info("************ test fail******************")

        self.driver.quit()

    @pytest.mark.regression
    def test_loginWithValidCredentials(self, setup):
        self.logger.info("*****************Test_002_Login******************")
        self.logger.info("*****************verifying login with valid credentials****************")
        self.driver = setup
        self.driver.get(self.base_url)

        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLoginButton()
        expected_title = "Codefios"
        actual_title = self.driver.title
        if expected_title == actual_title:
            self.logger.info("Login Successful")
            assert True, "Test Case Passed: Login Successful"
        else:
            # take a screenshot

            self.driver.save_screenshot('./Screenshots/LoginFailed.png')
            self.logger.info("************ test fail******************")

            assert False, "Test Case Failed: Login Failed"

        self.driver.quit()
