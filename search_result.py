from selenium.common import TimeoutException, StaleElementReferenceException
from config_reader import ConfigReader
from home_page import HomePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec


class SearchResult(ConfigReader, HomePage):
    FILTER = (By.XPATH, "//*[@id='sort_by_trigger']")
    ORDER = (By.XPATH, "//*[@id='Price_DESC']")
    TITLE = (By.XPATH, "//span[@class='title']")
    PRICE = (By.XPATH, "//div[contains(@class, 'final_price')]")
    SEARCHED = (By.XPATH, "//div//div[@data-tag_value='{}']")
    FIRST_RESULT_TITLE = (By.XPATH, "//span[@class='title']")

    def wait_for_background_color(self, locator, expected_color):
        def check_background_color(driver):
            element = self.wait.until(ec.presence_of_element_located(locator))
            actual_color = element.value_of_css_property('color')
            return actual_color == expected_color

        self.wait.until(check_background_color)

    def is_search_page_opened(self, game):
        searched_locator = (self.SEARCHED[0], self.SEARCHED[1].format(game))
        try:
            self.wait.until(
                ec.presence_of_element_located(searched_locator))
        except TimeoutException:
            return False
        return True

    def use_filter(self):

        initial_color = self.wait.until(
            ec.presence_of_element_located(self.FIRST_RESULT_TITLE)).value_of_css_property('color')
        button = self.wait.until(
            ec.element_to_be_clickable(self.FILTER)
        )
        button.click()

        button_order = self.wait.until(
            ec.element_to_be_clickable(self.ORDER)
        )
        button_order.click()

        self.wait_for_background_color(self.FIRST_RESULT_TITLE, initial_color)

    def get_data(self, n):
        result = {}
        try:
            titles = self.wait.until(ec.presence_of_all_elements_located(self.TITLE))
            prices = self.wait.until(ec.presence_of_all_elements_located(self.PRICE))
            self.wait.until(ec.visibility_of_all_elements_located(self.TITLE))

            for title, price in zip(titles, prices):
                if len(result) < n:
                    result[title.text] = price.text
                else:
                    return result
        except StaleElementReferenceException:
            return self.get_data(n)

        return result
