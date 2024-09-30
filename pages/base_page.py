from selenium.webdriver.support.ui import WebDriverWait
from utilites.config_reader import ConfigReader


class BasePage:
    cfg = ConfigReader()

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, self.cfg.return_value("TIMEOUT"))


