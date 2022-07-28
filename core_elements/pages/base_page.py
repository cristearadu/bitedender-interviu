from step_impl.utils import Driver


class BasePage:

    def __init__(self):
        self.driver = Driver.driver
