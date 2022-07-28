from getgauge.python import before_scenario, after_scenario
from step_impl.utils.init_driver import Driver
from settings import WEBSITE
from core_elements.pages.home_screen_page import Token


@before_scenario
def open_driver_before_scenario():
    Driver.init_driver()
    Driver.driver.get(WEBSITE)
    check_token()


@after_scenario
def close_driver_after_scenario():
    Driver.close_driver()


def check_token():
    if Driver.driver.check_exists(Token.TOKEN_BUTTON):
        token_screen = Token()
        token_screen.click_and_wait_for_token_to_disappear()
