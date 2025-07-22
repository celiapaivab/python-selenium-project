from selenium.webdriver.common.by import By

from pages.BasePage import  BasePage
from config.config import TestConfig

class LoginPageLocators:
    username_input =(By.ID, 'username')
    password_input = (By.ID, 'password')
    submit_button = (By.ID, 'submit')


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def login(self):
        self.driver.get(TestConfig.base_url)
        self.type_element(LoginPageLocators.username_input, TestConfig.username)
        self.type_element(LoginPageLocators.password_input, TestConfig.password)
        self.click_element(LoginPageLocators.submit_button)