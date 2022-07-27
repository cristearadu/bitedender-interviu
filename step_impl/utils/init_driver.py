import sys
from core_elements import CustomWebDriver


class Driver(object):
    driver: CustomWebDriver = None

    @staticmethod
    def init_driver():
        Driver.close_driver()
        if not Driver.driver:
            Driver.driver = CustomWebDriver()

    @staticmethod
    def close_driver():
        if Driver.driver:
            Driver.driver.close()
            Driver.driver = None
