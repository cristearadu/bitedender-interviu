from retry import retry
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from core_elements.logging_element import logger
from core_elements.models.elements import Button
from step_impl.utils import Driver


class Solutions:

    MULTIPLATFORM = (By.XPATH, '//a[@id="mp-scroll"]/span')

