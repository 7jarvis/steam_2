from selenium import webdriver


class WebDriverSingleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
            cls._instance = webdriver.Chrome()
        return cls._instance

    @staticmethod
    def quit():
        WebDriverSingleton._instance.quit()
        WebDriverSingleton._instance = None
