import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import StaleElementReferenceException


class SearchResult:
    def __init__(self, driver, game):
        self.driver = driver
        self.game = game
        self.TIMEOUT = 10
        self.searched = (
            By.XPATH, f"//div//div[@data-tag_value='{self.game}']")
        self.filer = (By.XPATH, "//a[@id='sort_by_trigger']")
        self.order = (By.XPATH, "//a[@id='Price_DESC']")
        self.title = (By.XPATH, "//span[@class='title']")
        self.price = (By.XPATH, "//div//div//div[contains(@class, 'final_price')]")

    def use_filter(self):
        button = WebDriverWait(self.driver, self.TIMEOUT).until(
            ec.element_to_be_clickable(self.filer)
        )
        button.click()

        button_order = WebDriverWait(self.driver, self.TIMEOUT).until(
            ec.element_to_be_clickable(self.order)
        )
        button_order.click()
        time.sleep(3)

    def retrieve_data(self, n):
        result = []
        prices = []
        for i in range(1, n + 1):
            element = f"({self.title[1]})[{i}]"
            price = f"({self.price[1]})[{i}]"
            try:
                title_element = WebDriverWait(self.driver, self.TIMEOUT).until(
                    ec.presence_of_element_located((By.XPATH, element)))
                result.append(title_element.text)
                price_element = WebDriverWait(self.driver, self.TIMEOUT).until(
                    ec.presence_of_element_located((By.XPATH, price)))
                prices.append(price_element.text)
            except StaleElementReferenceException:
                self.driver.execute_script("arguments[0].scrollIntoView();")

                title_element = WebDriverWait(self.driver, self.TIMEOUT).until(
                    ec.presence_of_element_located((By.XPATH, element))
                )
                result.append(title_element.text)
                price_element = WebDriverWait(self.driver, self.TIMEOUT).until(
                    ec.presence_of_element_located((By.XPATH, price)))
                prices.append(price_element.text)
        return result, prices

    @staticmethod
    def is_filtering_working(prices):
        check_prices = []
        for item in prices:
            value = item.split()
            for number in value:
                try:
                    number = float(number)
                    check_prices.append(number)
                except ValueError:
                    pass

        return all(check_prices[i] >= check_prices[i + 1] for i in range(len(check_prices) - 1))
