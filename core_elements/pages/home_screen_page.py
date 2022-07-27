from retry import retry
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from core_elements.logging_element import logger
from core_elements.models.elements import Button
from step_impl.utils import Driver


class HomeScreenPage:
    MAIN_MENU_LOGO = (By.XPATH, '//div[@id="MainMenu|BitdefenderLogo"]/a')
    HOME_SOLUTIONS_BUTTON = (By.XPATH, '//div[@id="Home"]/div/div[2]/div/a')

    def __init__(self):
        self.driver = Driver.driver

        self.driver.wait_for_element_to_be_visible(self.MAIN_MENU_LOGO)
        self.driver.wait_for_element_to_be_visible(self.HOME_SOLUTIONS_BUTTON)


class Token:
    TOKEN_BUTTON = (By.XPATH, '//a[@id="CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll"]')

    def __init__(self):
        self.driver = Driver.driver

    @retry(tries=3, delay=1)
    def click_token(self):
        Button(self.TOKEN_BUTTON).click()
