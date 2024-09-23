from home_page import ConfigReader
from home_page import HomePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time


class SearchResult(ConfigReader, HomePage):
    FILTER = (By.XPATH, "//*[@id='sort_by_trigger']")
    ORDER = (By.XPATH, "//*[@id='Price_DESC']")
    TITLE = (By.XPATH, "//span[@class='title']")
    PRICE = (By.XPATH, "//div[contains(@class, 'final_price')]")

    def is_search_page_opened(self, game):
        searched = (
            By.XPATH, f"//div//div[@data-tag_value='{game}']")
        tag = WebDriverWait(self.driver, self.TIMEOUT).until(
            ec.presence_of_element_located(searched))
        return True if tag else False

    def use_filter(self):
        first_element_before = WebDriverWait(self.driver, self.TIMEOUT).until(
            ec.presence_of_element_located(
                self.TITLE)
        ).text
        button = WebDriverWait(self.driver, self.TIMEOUT).until(
            ec.element_to_be_clickable(self.FILTER)
        )
        button.click()

        button_order = WebDriverWait(self.driver, self.TIMEOUT).until(
            ec.element_to_be_clickable(self.ORDER)
        )
        button_order.click()
        WebDriverWait(self.driver, self.TIMEOUT).until(
            ec.presence_of_element_located(self.ORDER)
        )

        WebDriverWait(self.driver, self.TIMEOUT).until(
            ec.text_to_be_present_in_element(self.TITLE, first_element_before)
        )

        WebDriverWait(self.driver, self.TIMEOUT).until(
            lambda x: WebDriverWait(x, self.TIMEOUT).until(
                ec.presence_of_element_located(self.TITLE)
            ).text != first_element_before
        )

    def retrieve_data(self, n):
        result = {}
        for i in range(1, n + 1):
            element = f"({self.TITLE[1]})[{i}]"
            price = f"({self.PRICE[1]})[{i}]"
            if ec.visibility_of_element_located((By.XPATH, element)):
                title_element = WebDriverWait(self.driver, self.TIMEOUT).until(
                    ec.presence_of_element_located((By.XPATH, element)))

                price_element = WebDriverWait(self.driver, self.TIMEOUT).until(
                    ec.presence_of_element_located((By.XPATH, price)))
                result[title_element.text] = price_element.text
            else:
                self.driver.execute_script("arguments[0].scrollIntoView();")
                title_element = WebDriverWait(self.driver, self.TIMEOUT).until(
                    ec.presence_of_element_located((By.XPATH, element))
                )

                price_element = WebDriverWait(self.driver, self.TIMEOUT).until(
                    ec.presence_of_element_located((By.XPATH, price)))
                result[title_element.text] = price_element.text

        return result
