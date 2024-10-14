from telnetlib import EC

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class LoginPage:
    textbox_username_id = "user_name"
    textbox_password_id = "password"
    button_login_xpath = "//*[@id='login_submit']"
    demo_logout_button = "/html/body/div[1]/header/nav/div[2]/ul[2]/li/a/img"


    def __init__(self, driver):
        self.driver = driver

    def setUsername(self, username):
        self.driver.find_element(By.ID, self.textbox_username_id).clear()  # Clear the existing text in the textbox
        self.driver.find_element(By.ID, self.textbox_username_id).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element(By.ID, self.textbox_password_id).clear() # Clear the existing text in the textbox
        self.driver.find_element(By.ID, self.textbox_password_id).send_keys(password)

    def clickLoginButton(self):
        self.driver.find_element(By.XPATH, self.button_login_xpath).click()

    def logout(self):

        logout = self.driver.find_element(By.XPATH, self.demo_logout_button)
        actions = ActionChains(self.driver)
        actions.move_to_element(logout).perform()
        log_out_button = self.driver.find_element(By.XPATH, "/html/body/div[1]/header/nav/div[2]/ul[2]/li/ul/li[2]/form/div/button")
        log_out_button.click()




