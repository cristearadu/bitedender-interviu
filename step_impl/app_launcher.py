import os
from getgauge.python import before_scenario, after_scenario
from step_impl.utils.driver import Driver
from settings import WEBSITE


@before_scenario
def open_driver_before_scenario():
    Driver.init_driver()
    Driver.driver.get(WEBSITE)
    check_token()


@after_scenario
def close_driver_after_scenario():
    Driver.close_driver()

def check_token():
    button = Driver.driver.find_element("xpath", '//a[@id="CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll"]')
    button.click()

