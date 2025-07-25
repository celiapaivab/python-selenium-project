from selenium.common import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def get_element(driver, by_locator):
    try:
        return WebDriverWait(driver, 10).until(EC.visibility_of_element_located(by_locator))
    except TimeoutException:
        print("The element {element} was not found in the page".format(element=by_locator))


class BasePage:
    def __init__(self, driver):
        self.driver =  driver

    def get_element(self, by_locator):
        return get_element(self.driver, by_locator)

    def get_element_text(self, by_locator):
        return get_element(self.driver, by_locator).text

    def type_element(self, by_locator, text):
        get_element(self.driver, by_locator).send_keys(text)

    def click_element(self, by_locator):
        get_element(self.driver, by_locator).click()

    def is_element_visible(self, by_locator):
        return get_element(self.driver, by_locator).is_displayed()
