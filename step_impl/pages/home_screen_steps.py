from getgauge.python import step
from selenium.webdriver.common.keys import Keys
from getgauge.python import custom_screenshot_writer
from core_elements.logging_element import logger
from step_impl.utils import Driver
from core_elements.pages.home_screen_page import HomeScreenPage


@step("Navigate to home screen -> See solutions")
def navigate_to_see_solutions():
    button = Driver.driver.find_element("xpath", '//div[@id="Home"]/div/div[2]/div/a')
    button.click()
