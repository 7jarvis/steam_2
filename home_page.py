import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class HomePage:

    def __init__(self, driver):
        self.driver = driver
        self.TIMEOUT = 10
        self.STEAM_LINK = 'https://store.steampowered.com/'
        self.INSTALL = (
            By.XPATH, "//div[@id='global_actions']//div[@id='global_action_menu']//a[contains(@class, 'installsteam')]")
        self.search_text = (
            By.XPATH, "//div[contains(@class, 'search')]//input[@id='store_nav_search_term']")
        self.search_button = (
            By.XPATH, "//div[contains(@class, 'search')]//a[@id='store_search_link']")

    def open_page(self, url):
        self.driver.get(url)

    def enter_game(self, game):
        search_input = WebDriverWait(self.driver, self.TIMEOUT).until(
            ec.presence_of_element_located(self.search_text)
        )
        search_input.clear()
        search_input.send_keys(game)

    def click_search(self):
        button = WebDriverWait(self.driver, self.TIMEOUT).until(
            ec.visibility_of_element_located(self.search_button)
        )
        self.driver.execute_script("arguments[0].click();", button)
