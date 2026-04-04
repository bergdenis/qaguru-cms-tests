import pytest
from selene import browser
from selenium import webdriver


@pytest.fixture(scope='session')
def setup_browser():
    options = webdriver.ChromeOptions()
    options.add_argument('--lang=en-US')
    options.add_experimental_option('prefs', {'intl.accept_languages': 'en,en_US'})
    browser.config.driver_options = options
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    yield
    browser.quit()
