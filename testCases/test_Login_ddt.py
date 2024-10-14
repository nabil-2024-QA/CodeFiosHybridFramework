import time

import pytest
import os
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utiliteis.ReadPropreties import read_config
from utiliteis.customLogger import LogGen


class Test_002_DDT_Login:
    base_url = read_config.get_base_url()
    path = "./TestData/codefios test1.xlsx"



    def setup_method(self):
        self.logger = LogGen.loggen()
        self.logger.info("Logger initialized.")


    @pytest.mark.regression
    def test_login_ddt(self,setup):
        list_status = []  # empty lis variable
        self.driver = setup
        self.driver.get(self.base_url)
        self.lp = LoginPage(self.driver)
        from utiliteis import XLUtils
        self.row_count = XLUtils.getRowCount(self.path, "Sheet1")
        self.column_count = XLUtils.getColumnCount(self.path, "Sheet1")
        print(self.row_count,self.column_count)
        for r in range(2, self.row_count + 1):
            self.username = XLUtils.readData(self.path, "Sheet1", r, 1)
            self.password = XLUtils.readData(self.path, "Sheet1", r, 2)
            self.expected = XLUtils.readData(self.path, "Sheet1", r, 3)

            self.lp.setUsername(self.username)
            self.lp.setPassword(self.password)
            self.lp.clickLoginButton()
            time.sleep(5)

            actual_title = self.driver.title
            expected_title = "Codefios"
            if expected_title == actual_title:
                if self.expected == "Pass":
                    self.lp.logout()
                    time.sleep(5)
                    list_status.append("Pass")
                    print("test pass")
                elif self.expected == "Fail":
                    list_status.append("Fail")
                    print("test fail")
            elif actual_title != expected_title:
                 if self.expected == "Pass":
                     list_status.append("Fail")
                     print("test fail")
                 elif self.expected == "Fail":
                     list_status.append("Pass")
                     print("test pass")
        if "fail" not in list_status:
                self.logger.info("All test cases passed")
                self.driver.close()
                assert True, "All test cases passed"
        else:
                self.logger.info("Test case failed")
                assert True, "All test cases passed"
                assert False, "Test case failed"
                self.driver.close()