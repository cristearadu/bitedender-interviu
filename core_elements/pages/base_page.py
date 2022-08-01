from step_impl.utils import Driver


class BasePage:
    """
    Base page to init same elements POM classes
    """
    def __init__(self):
        self.driver = Driver.driver
