from getgauge.python import step
from core_elements.pages.solutions_page import Solutions
from core_elements.pages.cart_page import Cart
from core_elements.logging_element import logger
from step_impl.utils import Driver
from getgauge.python import data_store
from settings import Timeouts


@step("Find and click Multiplatform")
def find_and_click_multiplatform():
    solutions_page = Solutions()
    solutions_page.click_multiplaform()


@step("Click on buy product <product>")
def click_on_buy_product(product):
    solutions_page = Solutions()
    logger.info(f"Buying product {product}")
    solutions_page.click_cumpara_premium_security()
    assert Driver.driver.check_exists(Cart.FINAL_PRICE, timeout=Timeouts.WAIT_TO_DISAPPEAR), "Failed to load \'Cart\' page"


@step("Store prices for <product>")
def store_prices_for_product(product):
    logger.info(f"Storing the price for {product}")

    solutions_page = Solutions()
    prices = solutions_page.get_price_information_premium_security()

    for key, value in prices.items():
        assert value, f"Failed to retrieve any value for {key}"
        logger.info(f"The value for {key} is: {value}")

    logger.info("Storing prices to DataStore")
    data_store.scenario['prices'] = prices
    logger.info(f"Storing product to DataStore: {product}")
    data_store.scenario['product_name'] = product


"""
                ###### VERIFY/ASSERTS STEPS ######
"""


@step("Verify if <text_to_verify> is selected for multiplatform")
def verify_text_is_selected(text_to_verify):
    solutions_page = Solutions()
    premium_security = solutions_page.premium_security
    assert premium_security.text == text_to_verify, f"Failed to find the selected text: {text_to_verify}. " \
                                                    f"Found {premium_security.text}"
    logger.info(f"{premium_security.text} has been selected")
