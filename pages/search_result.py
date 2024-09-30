from selenium.common import TimeoutException
from utilites.config_reader import ConfigReader
from pages.home_page import HomePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec


class SearchResult(ConfigReader, HomePage):
    FILTER = (By.XPATH, "//*[@id='sort_by_trigger']")
    ORDER = (By.XPATH, "//*[@id='Price_DESC']")
    TITLE = (By.XPATH, "//span[@class='title']")
    PRICE = (By.XPATH, "//div[contains(@class, 'final_price')]")
    SEARCHED = (By.XPATH, "//div//div[@data-tag_value='{}']")
    FIRST_RESULT_TITLE = (By.XPATH, "//span[@class='title']")

    def _check_style_attribute(self, locator):
        element = self.wait.until(ec.presence_of_element_located(locator))
        style_value = element.get_attribute('style')

        return style_value == ''

    def is_search_page_opened(self, game):
        searched_locator = (self.SEARCHED[0], self.SEARCHED[1].format(game))
        try:
            self.wait.until(
                ec.presence_of_element_located(searched_locator))
        except TimeoutException:
            return False
        return True

    def use_filter(self):

        button = self.wait.until(
            ec.element_to_be_clickable(self.FILTER)
        )
        button.click()

        button_order = self.wait.until(
            ec.element_to_be_clickable(self.ORDER)
        )
        button_order.click()

        self._check_style_attribute(self.FIRST_RESULT_TITLE)

    def get_data(self, n):
        result = {}

        self.wait.until(ec.visibility_of_all_elements_located(self.TITLE))

        while len(result) < n:
            titles = self.wait.until(ec.presence_of_all_elements_located(self.TITLE))
            prices = self.wait.until(ec.presence_of_all_elements_located(self.PRICE))

            for i in range(len(titles)):
                if len(result) < n:
                    title = self.wait.until(ec.visibility_of(titles[i]))
                    price = self.wait.until(ec.visibility_of(prices[i]))

                    result[title.text] = price.text
                else:
                    return result

        return result
