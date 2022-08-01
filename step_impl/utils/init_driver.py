import sys
from core_elements import CustomWebDriver


class Driver:
    """Final Driver class that is used for the framework"""
    driver: CustomWebDriver = None

    @staticmethod
    def init_driver():
        sys.stdout.reconfigure(encoding='utf-8')  # to make romanian characters readable
        Driver.close_driver()
        if not Driver.driver:
            Driver.driver = CustomWebDriver()

    @staticmethod
    def close_driver():
        if Driver.driver:
            Driver.driver.close()
            Driver.driver = None
