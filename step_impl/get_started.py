import os
import chromedriver_autoinstaller
from getgauge.python import before_suite, after_suite, step
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from uuid import uuid1
from getgauge.python import custom_screenshot_writer
from core_elements.logging_element import logger
from settings import ROOT_WORKING_DIRECTORY

class Driver:
    instance = None

@before_suite
def init():
    global driver
    """
    ChromeDriver will be automatically installed for a specific section
    Why? To not depend on a specific version for your browser, to not download after a Google Chrome update another
    version of ChromeDriver
    """
    chromedriver_autoinstaller.install()
    Driver.instance = webdriver.Chrome()
    Driver.instance.get("https:\\google.com")

@after_suite
def close():
    Driver.instance.close()

@step("Search for <query>")
def go_to_get_started_page(query):
    logger.info("Searching for first element")
    button = Driver.instance.find_element("xpath", '//*[@id="L2AGLb"]/div')
    button.click()
    textbox = Driver.instance.find_element("xpath", "//input[@name='q']")
    logger.info(f"Sending {query}")
    textbox.send_keys(query)
    textbox.send_keys(Keys.RETURN)
    # take_screenshot()

# # Return a screenshot file name
# @custom_screenshot_writer
# def take_screenshot():
#     image = Driver.instance.get_screenshot_as_png()
#     file_name = os.path.join(os.getenv("gauge_screenshots_dir"), "screenshot-{0}.png".format(uuid1().int))
#     file = open(file_name, "wb")
#     file.write(image)
#     return os.path.basename(file_name)
