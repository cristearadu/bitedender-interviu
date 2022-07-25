from getgauge.python import step
from selenium.webdriver.common.keys import Keys
from getgauge.python import custom_screenshot_writer
from core_elements.logging_element import logger
from step_impl.utils import Driver


# @step("Search for <query>")
# def go_to_get_started_page(query):
#     logger.info("Searching for first element")
#     button = Driver.driver.find_element("xpath", '//a[@id="CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll"]')
#     button.click()
#     # textbox = Driver.driver.instance.find_element("xpath", "//input[@name='q']")
#     # logger.info(f"Sending {query}")
#     # textbox.send_keys(query)
#     # textbox.send_keys(Keys.RETURN)
#     # take_screenshot()

# # Return a screenshot file name
# @custom_screenshot_writer
# def take_screenshot():
#     image = Driver.instance.get_screenshot_as_png()
#     file_name = os.path.join(os.getenv("gauge_screenshots_dir"), "screenshot-{0}.png".format(uuid1().int))
#     file = open(file_name, "wb")
#     file.write(image)
#     return os.path.basename(file_name)
