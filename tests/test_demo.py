import time

from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
from support.common import get_element, get_element_text, type_element, click_element, is_element_visible


@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.close()
    driver.quit()

def test_verify_tittle(driver):
    driver.get("http://dbankdemo.com/bank/login")
    assert "Digital Bank" == driver.title

def test_login(driver):
    # find username element input and type jsmith@demo.io
    # driver.find_element(By.ID, 'username').send_keys('jsmith@demo.io')
    type_element(driver, (By.ID, 'username'), 'jsmith@demo.io')

    # find password element input and type Demo123!
    # driver.find_element(By.ID, 'password').send_keys('Demo123!')
    type_element(driver, (By.ID, 'password'), 'Demo123!')

    # click sign in button
    # driver.find_element(By.ID, 'submit').click()
    click_element(driver, (By.ID, 'submit'))
    time.sleep(2)
    assert 'home' in driver.current_url

def test_verify_version(driver):
    # click on about link button
    get_element(driver, (By.ID, 'aboutLink')).click()
    # verify version within the popup dialog
    assert 'Version:' in get_element_text(driver, (By.CLASS_NAME, 'modal-body'))