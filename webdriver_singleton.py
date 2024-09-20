from selenium import webdriver
from threading import Lock


class WebDriverSingleton:
    _instance = None
    _lock = Lock()

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = webdriver.Chrome()
        return cls._instance

    @classmethod
    def quit(cls):
        if cls._instance is not None:
            cls._instance.quit()
            cls._instance = None
