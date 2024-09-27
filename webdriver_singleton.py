from selenium import webdriver


class WebDriverSingleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
            cls._instance.driver = webdriver.Chrome()
        return cls._instance

    @staticmethod
    def clear():
        WebDriverSingleton._instance.driver.quit()
        WebDriverSingleton._instance = None
