import yaml

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class ConfigReader:
    with open("config_file.yml", "r") as f:
        config = yaml.safe_load(f)["config"]
    TIMEOUT = config["TIMEOUT"]
    STEAM_LINK = config["STEAM_LINK"]


class HomePage:
    cfg = ConfigReader()
    INSTALL = (
        By.XPATH, "//div[@id='global_actions']//div[@id='global_action_menu']//a[contains(@class, 'installsteam')]")
    SEARCH_TEXT = (
        By.XPATH, "//div[contains(@class, 'search')]//input[@id='store_nav_search_term']")
    SEARCH_BUTTON = (
        By.XPATH, "//div[contains(@class, 'search')]//a[@id='store_search_link']")

    def __init__(self, driver):
        self.driver = driver

    def is_homepage_opened(self):
        install_button = WebDriverWait(self.driver, self.cfg.TIMEOUT).until(
            ec.element_to_be_clickable(self.INSTALL))
        return True if install_button else False

    def enter_game(self, game):
        search_input = WebDriverWait(self.driver, self.cfg.TIMEOUT).until(
            ec.presence_of_element_located(self.SEARCH_TEXT)
        )
        search_input.clear()
        search_input.send_keys(game)

    def click_search(self):
        button = WebDriverWait(self.driver, self.cfg.TIMEOUT).until(
            ec.visibility_of_element_located(self.SEARCH_BUTTON)
        )
        self.driver.execute_script("arguments[0].click();", button)
