import os

import pytest
from selenium import webdriver

@pytest.fixture(scope='class')
def driver(request):
    driver = webdriver.Chrome()
    driver.maximize_window()
    request.cls.driver = driver

    yield driver

    driver.close()
    driver.quit()
