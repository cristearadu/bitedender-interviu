from retry import retry
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementNotInteractableException, ElementClickInterceptedException
from settings import Timeouts
from step_impl.utils import Driver
from core_elements.logging_element import logger


class WebElement(object):

    def __init__(self, locator, timeout=Timeouts.MEDIUM):
        self.driver = Driver.driver
        self.locator = locator
        self.timeout = timeout
        self.wait = WebDriverWait(self.driver, timeout)
        self.wait.until(EC.visibility_of_element_located(self.locator))

    @property
    def element(self):
        """Returns a WebElement object"""
        return self.driver.find_element(*self.locator)

    @property
    def text(self):
        return self.element.text

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

    def __init__(self, locator, timeout=Timeouts.MEDIUM):
        super(Button, self).__init__(locator=locator, timeout=timeout)
        self.driver.wait_for_element_to_be_clickable(self.locator)

    @retry(tries=3, delay=1)
    def click(self, check_element=False):
        self.scroll_to_element()
        try:
            self.element.click()
            if check_element:
                logger.info(f"Checking if element {self.locator} has been correctly pressed")
                if self.driver.check_exists(self.locator, timeout=Timeouts.SMALL):
                    self.element.click()

        except ElementClickInterceptedException:
            logger.error("Failed to click on element with Selenium Click.")
            self.javascript_click()

    def javascript_click(self):
        logger.info("Trying to click with JavaScript click")
        self.driver.execute_script("arguments[0].click();", self.element)


class TextBox(WebElement):

    def __init__(self, locator, timeout=Timeouts.MEDIUM):
        super(TextBox, self).__init__(locator=locator, timeout=timeout)

        self.driver.wait_for_element_to_be_clickable(locator)

    @property
    def contents(self):
        return self.element.text

    @contents.setter
    @retry(tries=3, delay=1)
    def contents(self, value):
        try:
            self.element.clear()
            self.element.send_keys(value)
        except ElementNotInteractableException:
            logger.error("The element is a READONLY Textbox")

    def clear(self):
        self.element.clear()

    def send_keys(self, value):
        self.element.send_keys(value)
