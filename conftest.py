import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options
from config import Config


@allure.step('Открытие браузера / переход на страницу сервиса / закрытие браузера')
@pytest.fixture(scope='function')
def driver():
    firefox_options = Options()
    firefox_options.add_argument("--width=1920")
    firefox_options.add_argument("--height=1080")
    driver = webdriver.Firefox(options=firefox_options)
    driver.get(Config.MAIN_PAGE_SCOOTER)
    yield driver
    driver.quit()
