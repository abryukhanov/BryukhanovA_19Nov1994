from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from page.AltaivitaMainPage import MainPage
from page.AltaivitaCartPage import CartPage
from api.AltaivitaApiPage import AltaivitaApi
import pytest
from config import config 

base_url_ui = config.get("base_url_ui")
base_url_api = config.get("base_url_api")


@pytest.fixture
def browser():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get(base_url_ui)
    driver.implicitly_wait(4)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture
def main_page(browser):
    return MainPage(browser)


@pytest.fixture
def cart_page(browser):
    return CartPage(browser)


@pytest.fixture
def api():
    return AltaivitaApi(base_url_api)