from getgauge.python import step
from core_elements.pages.cart_page import Cart
from core_elements.logging_element import logger
from getgauge.python import data_store
from core_elements.algos import check_same_currency

"""
                ###### VERIFY/ASSERTS STEPS ######
"""


@step("Verify that product name is correct")
def verify_product_name():
    cart_page = Cart()
    logger.info("Reading product name from cart")
    cart_product_name = cart_page.product_name.contents
    logger.info(f"Product name is: {cart_product_name}")

    try:
        assert data_store.scenario['product_name'].lower() in cart_product_name.lower(), \
            f"Failed to match the product on cart." \
            f"\nExpected results: {cart_product_name}" \
            f"\nActual results: {data_store['product_name']}"

    except KeyError as e:
        raise KeyError(f"Failed to find the expected key in data_store dictionary: {repr(e)}")

    except AttributeError as e:
        raise AttributeError(f"Wrong data type for data_store or cart_product_name for .lower() function: {repr(e)}")

    logger.info("Product name has been set correctly")


@step("Verify the correct price and product has been displayed in cart")
def verify_correct_data():
    cart_page = Cart()
    logger.info("Reading product price from cart")
    cart_prices = cart_page.get_price_information_one_product()
    logger.info(f"Cart prices: {cart_prices}")

    try:
        for price_type, price_value in cart_prices.items():

            assert check_same_currency(price_value, data_store.scenario['prices'][price_type]), \
                f"Failed to match the currency for product in cart for {price_type}." \
                f"\nExpected results: {price_value}" \
                f"\nActual results: {data_store.scenario['prices'][price_type]}"

            assert price_value == data_store.scenario['prices'][price_type], \
                f"Failed to match the price for product in cart for {price_type}." \
                f"\nExpected results: {price_value}" \
                f"\nActual results: {data_store.scenario['prices'][price_type]}"

    except KeyError as e:
        raise KeyError(f"Failed to find the expected key in data_store dictionary: {repr(e)}")
