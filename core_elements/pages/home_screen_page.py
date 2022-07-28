from retry import retry
from selenium.webdriver.common.by import By
from core_elements.models.elements import Button
from step_impl.utils import Driver
from core_elements.project_decorators import log_click_button


class HomeScreenPage:
    MAIN_MENU_LOGO = (By.XPATH, '//div[@id="MainMenu|BitdefenderLogo"]/a')
    HOME_SOLUTIONS_BUTTON = (By.XPATH, '//div[@id="Home"]/div/div[2]/div/a')

    def __init__(self):
        self.driver = Driver.driver

        self.driver.wait_for_element_to_be_visible(self.MAIN_MENU_LOGO)
        self.driver.wait_for_element_to_be_visible(self.HOME_SOLUTIONS_BUTTON)

    @retry(tries=3, delay=1)
    @log_click_button
    def click_home_solutions_button(self):
        return Button(self.HOME_SOLUTIONS_BUTTON).click()


class Token:
    TOKEN_BUTTON = (By.XPATH, '//a[@id="CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll"]')

    def __init__(self):
        self.driver = Driver.driver

    @retry(tries=3, delay=1)
    @log_click_button
    def click_token(self):
        Button(self.TOKEN_BUTTON).click()

    def click_and_wait_for_token_to_disappear(self):
        self.click_token()
        self.driver.wait_for_element_to_be_invisible(self.TOKEN_BUTTON)
