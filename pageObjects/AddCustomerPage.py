from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class AddCustomer:
    lnkcustomers_Button_xpath = "//span[normalize-space()='Customers']"
    lnkadd_customer_Button_xpath = "//span[normalize-space()='Add Customer']"
    txtfull_name_Button_xpath = "//input[@name='name']"
    btn_Addcompany_xpath = "//button[normalize-space()='Add Company']"
    txtcompanyName_xpath = "//input[@id='company_name']"
    txtURL_xpath = "//input[@id='company_url']"
    txtcompanyEmail_xpath = "//input[@id='company_email']"
    numcompanyphone_xpath = "//input[@id='company_phone']"
    txtlogoUrl_xpath = "//input[@id='logo_url']"
    btn_new_company_xpath = "//button[@id='companyformsubmit']"
    list_company_xpath = "//*[@id='general_compnay']/div[2]/div/select"
    txtemail_textbox_xpath = "//input[@name='email']"
    numphone_textbox_xpath = "//input[@id='phone']"
    txtaddress_textbox_path = "//input[@name='address']"
    txtcity_textbox_xpath = "//input[@name='city']"
    numzipCode_xpath = "//*[@id='port']"
    drpcountry_drpdown_textbox_xpath = "//*[@id='general_compnay']/div[8]/div[1]/select"
    drpgroup_drpdown_xpath = "//*[@id='customer_group']"
    save_btn = "//*[@id='save_btn']"
    def __init__(self, driver):
        self.driver = driver

    def wait_for_element_to_be_visible(self, xpath, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located((By.XPATH, xpath))
        )

    def clickCustomersLink(self):
        self.wait_for_element_to_be_visible(self.lnkcustomers_Button_xpath).click()

    def clickAddCustomerLink(self):
        self.wait_for_element_to_be_visible(self.lnkadd_customer_Button_xpath).click()

    def enterFullName(self, full_name):
        full_name_field = self.wait_for_element_to_be_visible(self.txtfull_name_Button_xpath)
        full_name_field.clear()
        full_name_field.send_keys(full_name)

    def addCompany(self):
        self.wait_for_element_to_be_visible(self.btn_Addcompany_xpath).click()

    def enterCompanyName(self, company_name):
        company_name_field = self.wait_for_element_to_be_visible(self.txtcompanyName_xpath)
        company_name_field.clear()
        company_name_field.send_keys(company_name)

    def enterURL(self, url):
        url_field = self.wait_for_element_to_be_visible(self.txtURL_xpath)
        url_field.clear()
        url_field.send_keys(url)

    def enterCompanyEmail(self, email):
        email_field = self.wait_for_element_to_be_visible(self.txtcompanyEmail_xpath)
        email_field.clear()
        email_field.send_keys(email)

    def enterCompanyPhone(self, phone):
        phone_field = self.wait_for_element_to_be_visible(self.numcompanyphone_xpath)
        phone_field.clear()
        phone_field.send_keys(phone)

    def enterLogoUrl(self, logo_url):
        logo_url_field = self.wait_for_element_to_be_visible(self.txtlogoUrl_xpath)
        logo_url_field.clear()
        logo_url_field.send_keys(logo_url)

    def clickNewCompanyButton(self):
        self.wait_for_element_to_be_visible(self.btn_new_company_xpath).click()

    def selectCompany(self, company_name):
        companies = self.wait_for_element_to_be_visible(self.list_company_xpath)
        select_company = Select(companies)
        select_company.select_by_visible_text(company_name)

    def enterEmail(self, email):
        email_field = self.wait_for_element_to_be_visible(self.txtemail_textbox_xpath)
        email_field.clear()
        email_field.send_keys(email)

    def enterPhone(self, phone):
        phone_field = self.wait_for_element_to_be_visible(self.numphone_textbox_xpath)
        phone_field.clear()
        phone_field.send_keys(phone)

    def enterAddress(self, address):
        address_field = self.wait_for_element_to_be_visible(self.txtaddress_textbox_path)
        address_field.clear()
        address_field.send_keys(address)

    def enterCity(self, city):
        city_field = self.wait_for_element_to_be_visible(self.txtcity_textbox_xpath)
        city_field.clear()
        city_field.send_keys(city)

    def enterZipCode(self, zip_code):
        zip_code_field = self.wait_for_element_to_be_visible(self.numzipCode_xpath)
        zip_code_field.clear()
        zip_code_field.send_keys(zip_code)

    def selectCountry(self, country_name):
        select_element = self.wait_for_element_to_be_visible(self.drpcountry_drpdown_textbox_xpath)
        select_country = Select(select_element)

        # Log available options
        options = [option.text for option in select_country.options]
        print(f"Available options: {options}")  # Check what options are available

        select_country.select_by_visible_text(country_name)

    def selectGroup(self, group_name):
        groups = self.wait_for_element_to_be_visible(self.drpgroup_drpdown_xpath)
        select_group = Select(groups)
        select_group.select_by_visible_text(group_name)

    def clickSaveButton(self):
        self.wait_for_element_to_be_visible(self.save_btn).click()