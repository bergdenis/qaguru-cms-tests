import pytest
from selene import browser
from selenium import webdriver


@pytest.fixture(scope='function', autouse=True)
def browser_management():
    browser.config.base_url = 'https://demoqa.com/automation-practice-form/'
    browser.config.timeout = 4.0
    browser.config.driver_options = webdriver.ChromeOptions()

    yield

    browser.quit()
