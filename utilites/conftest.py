import pytest
from webdriver_singleton import WebDriverSingleton


@pytest.fixture()
def driver():
    driver = WebDriverSingleton()
    driver.maximize_window()
    yield driver
    driver.quit()
    WebDriverSingleton._instance = None
