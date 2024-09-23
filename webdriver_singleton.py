from selenium import webdriver


class WebDriverSingleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(WebDriverSingleton, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        if not hasattr(self, '_initialized'):
            self._initialized = True
            self.driver = webdriver.Chrome()

    @classmethod
    def get_instance(cls):
        return cls()

    def quit(self):
        if self.driver:
            self.driver.quit()
            WebDriverSingleton._instance = None
