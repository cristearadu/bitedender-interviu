from retry import retry
from selenium.webdriver.common.by import By
from core_elements.models.elements import Button, TextBox
from core_elements.project_decorators import log_click_button
from core_elements.pages.base_page import BasePage


class Cart(BasePage):

    FINAL_PRICE = (By.XPATH, '//section[@id="section8"]/div/div[2]/div[2]/span')
    OLD_PRICE = (By.XPATH, '//section[@id="section1"]/div/div/div[2]/div[2]/span')
    PRODUCT_NAME = (By.XPATH, '//section[@id="section1"]/div/div/div[1]/div[2]/span[1]')
    REMOVE_PRODUCT = (By.XPATH, '//section[@id="section1"]/div/div/div[2]/div[2]/span/../../div/span/i')

    def __init__(self):
        super(Cart, self).__init__()

        self.driver.wait_for_element_to_be_visible(self.FINAL_PRICE)

    @retry(tries=3, delay=1)
    @log_click_button
    def click_remove_product(self):
        Button(self.REMOVE_PRODUCT).click()

    @property
    def product_name(self):
        return TextBox(self.PRODUCT_NAME)

    @property
    def old_price(self):
        return TextBox(self.OLD_PRICE)

    @property
    def final_price(self):
        return TextBox(self.FINAL_PRICE)

    def get_price_information_one_product(self):
        """
        Returns dictionary with price information for one product on cart
        All values are 'STR'
        """
        return {'old_price': self.old_price.contents,
                'last_price': self.final_price.contents
                }
