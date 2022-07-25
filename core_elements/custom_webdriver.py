import os
from selenium.common.exceptions import WebDriverException, NoSuchFrameException, TimeoutException
from selenium import webdriver
from settings import Timeouts
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


class CustomWebDriver(webdriver.Chrome):
    def __init__(self):

        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("start-maximized")
        chrome_options.add_argument("--disable-blink-features=AutomationControlled")

        super().__init__(executable_path='chromedriver',
                         service=Service(ChromeDriverManager().install()),
                         options=chrome_options)

        self.implicitly_wait(Timeouts.IMPLICITLY_WAIT)

