from getgauge.python import step
from selenium.webdriver.common.keys import Keys
from getgauge.python import custom_screenshot_writer
from core_elements.logging_element import logger
from step_impl.utils import Driver

from app_launcher import open_driver_before_scenario, close_driver_after_scenario


@step("Navigate to home screen -> See solutions")
def navigate_to_see_solutions():
    import pdb; pdb.set_trace()
    button = Driver.driver.find_element("xpath", '//a[@id="CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll"]')
    button.click()
