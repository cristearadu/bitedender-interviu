from retry import retry
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from settings import Timeouts
from step_impl.utils import Driver


class WebElement(object):

    def __init__(self, locator, parent_locator=None, timeout=Timeouts.MEDIUM):
        self.driver = Driver.driver
        self.locator = locator
        self.wait = WebDriverWait(self.driver, timeout)
        self.parent_locator = parent_locator
        self.wait.until(EC.visibility_of_element_located(self.locator))

    @property
    def element(self):
        """Returns a WebElement object"""
        if self.parent_locator:
            return self.driver.find_element(*self.parent_locator).find_element(*self.locator)
        else:
            return self.driver.find_element(*self.locator)

    def scroll_to_element(self):
        """Scroll to element"""
        self.driver.execute_script('arguments[0].scrollIntoView(true);', self.element)

    def find_element(self, locator):
        """Selenium find_element method"""
        self.driver.find_element(*locator)

    def is_enabled(self):
        return self.element.is_enabled()

    def is_displayed(self):
        return self.element.is_displayed()


class Button(WebElement):

    def __init__(self, locator, parent_locator=None, timeout=Timeouts.MEDIUM):
        super(Button, self).__init__(locator=locator, parent_locator=parent_locator, timeout=timeout)
        Driver.driver.wait_for_element_to_be_clickable(self.locator)

    @retry(tries=3, delay=1)
    def click(self):
        self.scroll_to_element()
        self.element.click()
