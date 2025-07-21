import pytest
from pages.LoginPage import LoginPage

@pytest.mark.usefixtures("driver")
class BaseTest:
    def setup_method(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.login()

    def teardown_method(self):
        print("test teardown")
