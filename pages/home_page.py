from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from pages.base_page import BasePage
from selenium.common.exceptions import TimeoutException


class HomePage(BasePage):
    INSTALL = (
        By.XPATH, "//*[@id='global_actions']//*[@id='global_action_menu']//a[contains(@class, 'installsteam')]")
    SEARCH_TEXT = (
        By.XPATH, "//div[contains(@class, 'search')]//input[@id='store_nav_search_term']")
    SEARCH_BUTTON = (
        By.XPATH, "//div[contains(@class, 'search')]//*[@id='store_search_link']")

    def is_page_opened(self):
        try:
            WebDriverWait(self.driver, self.cfg.return_value("TIMEOUT")).until(
                ec.element_to_be_clickable(self.INSTALL))
        except TimeoutException:
            return False
        return True

    def enter_game(self, game):
        search_input = self.wait.until(
            ec.presence_of_element_located(self.SEARCH_TEXT)
        )
        search_input.clear()
        search_input.send_keys(game)

    def click_search(self):
        button = self.wait.until(
            ec.visibility_of_element_located(self.SEARCH_BUTTON)
        )
        self.driver.execute_script("arguments[0].click();", button)
