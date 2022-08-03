from retry import retry
from selenium.webdriver.common.by import By
from core_elements.models.elements import Button, TextBox
from core_elements.project_decorators import log_click_button
from core_elements.pages.base_page import BasePage
from settings import Timeouts


class Solutions(BasePage):

    # MULTIPLATFORM = (By.XPATH, '//a[@id="mp-scroll"]/span') # until 03 August
    MULTIPLATFORM = (By.XPATH, '//div[@id="container-c623da4f75"]/div/div[5]/section/div/div[2]/a[5]/img')

    # Until 3 August
    # PREMIUM_SECURITY = (By.XPATH, '//div[@id="MultiplatformSecurity"]//h3[contains(text(), "PREMIUM SECURITY")]')
    # PRICE_INFORMATION = (By.XPATH, f'{PREMIUM_SECURITY[1]}/../div/span')
    # BUY_PREMIUM_SECURITY = (By.XPATH, f'{PREMIUM_SECURITY[1]}/..//a[contains(text(), "Cumpără")]')
    # BUY_PREMIUM_SECURITY_2 = (By.XPATH, '//div[@id="MultiplatformSecurity"]/div[2]/div[1]/a[1]')

    # I could have taken the xpath much more easier than using ;contains text(), but I wanted to show you that
    # I know how to find an element after text
    PREMIUM_SECURITY = (By.XPATH, '//section[@id="multiplatform"]//h4[contains(text(), "Premium Security")]')
    OLD_PRICE_INFORMATION = (By.XPATH, f'{PREMIUM_SECURITY[1]}/../../../div/div/label/del')
    NEW_PRICE_INFORMATION = (By.XPATH, f'{PREMIUM_SECURITY[1]}/../../../div/div/div/h4')
    BUY_PREMIUM_SECURITY = (By.XPATH, '//section[@id="multiplatform"]/div/div/div[2]/div[2]/div[3]/a[1]/span')

    def __init__(self):
        super(Solutions, self).__init__()

        self.driver.wait_for_element_to_be_visible(self.MULTIPLATFORM, timeout=Timeouts.MEDIUM)

    @retry(tries=3, delay=1)
    @log_click_button
    def click_multiplaform(self):
        Button(self.MULTIPLATFORM).click()

    @property
    def premium_security(self):
        return TextBox(self.PREMIUM_SECURITY)

    @property
    def buy_premium_security(self):
        return Button(self.BUY_PREMIUM_SECURITY)

    @retry(tries=3, delay=1)
    @log_click_button
    def click_cumpara_premium_security(self):
        self.buy_premium_security.click(check_element=True)

    @property
    def old_price(self):
        return TextBox(self.OLD_PRICE_INFORMATION)

    @property
    def new_price(self):
        return TextBox(self.NEW_PRICE_INFORMATION)

    def get_price_information_premium_security(self):
        """
        Returns dictionary with price information for 'PREMIUM SECURITY'
        All values are 'STR'
        """
        return {'old_price': self.old_price.contents,
                'last_price': self.new_price.contents
                }
