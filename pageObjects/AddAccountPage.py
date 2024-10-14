from selenium import webdriver
from selenium.webdriver.common.by import By


class addAccount:
    listAccount_xpath = "//span[normalize-space()='List Accounts']"
    addAccount_xpath = "//button[normalize-space()='Add Account']"
    accountName_xpath = "//input[@id='account_name']"
    description_xpath = "//textarea[@id='description']"
    balance_xpath = "//input[@id='balance']"
    account_number_xpath = "//input[@id='account_number']"
    contactPerson_xpath = "//input[@id='contact_person']"
    saveButtonAddAccount_xpath = "//button[@id='accountSave']"

    def __init__(self, driver):
             self.driver = driver
             self.driver.implicitly_wait(10)


    def add_account(self, account_name,description,balance,account_number,contact_person):
           self.driver.find_element(By.XPATH, self.listAccount_xpath).click()
           self.driver.find_element(By.XPATH, self.addAccount_xpath).click()
           self.driver.find_element(By.XPATH, self.accountName_xpath).send_keys(account_name)
           self.driver.find_element(By.XPATH, self.description_xpath).send_keys(description)
           self.driver.find_element(By.XPATH, self.balance_xpath).send_keys(balance)
           self.driver.find_element(By.XPATH, self.account_number_xpath).send_keys(account_number)
           self.driver.find_element(By.XPATH, self.contactPerson_xpath).send_keys(contact_person)
           self.driver.find_element(By.XPATH, self.saveButtonAddAccount_xpath).click()


