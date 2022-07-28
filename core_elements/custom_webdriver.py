from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from settings import Timeouts


class CustomWebDriver(webdriver.Chrome):

    ELEMENT_NOT_FOUND = (
        "Element with locator {} was not found. Timeout = {} seconds")

    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("start-maximized")
        chrome_options.add_argument("--disable-blink-features=AutomationControlled")

        super().__init__(executable_path='chromedriver',
                         service=Service(ChromeDriverManager().install()),
                         options=chrome_options)

        self.implicitly_wait(Timeouts.IMPLICITLY_WAIT)

    def wait_for_element_to_be_invisible(self, locator, timeout: int = Timeouts.WAIT_TO_DISAPPEAR):
        WebDriverWait(self, timeout).until(EC.invisibility_of_element_located(locator))

    def wait_for_element_to_be_visible(self, locator, timeout: int = Timeouts.TIMEOUT_DEFAULT):
        WebDriverWait(self, timeout).until(EC.visibility_of_element_located(locator))

    def wait_for_element_to_be_clickable(self, locator, timeout: int = Timeouts.TIMEOUT_DEFAULT):
        WebDriverWait(self, timeout).until(EC.element_to_be_clickable(locator))

    def check_exists(self, locator, timeout: int = Timeouts.TIMEOUT_DEFAULT):
        """
        Return True if element has been located, else returns False
        """
        try:
            WebDriverWait(self, timeout).until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            return False
        return True
####################################################################################################################
    """
    Unused functions for webdriver, but implemented for framework
    """

    def open_new_tab(self, url: str):
        self.execute_script(f'window.open("{url}", "_blank");')

    def switch_tab(self, tab_number: int):
        self.switch_to.window(self.window_handles[tab_number - 1])
