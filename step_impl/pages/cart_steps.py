from getgauge.python import step
from core_elements.pages.cart_page import Cart
from core_elements.pages.solutions_page import Solutions
from core_elements.logging_element import logger
from getgauge.python import data_store
from core_elements.algos import CurrencyFunctions
from step_impl.utils import Driver


@step("Delete the product from cart")
def delete_product_from_cart():
    cart_page = Cart()
    logger.info("Removing the product")
    cart_page.click_remove_product()


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
def verify_price_and_data_on_cart():
    cart_page = Cart()
    logger.info("Reading product price from cart")
    cart_prices = cart_page.get_price_information_one_product()
    logger.info(f"Cart prices: {cart_prices}")

    currency_function = CurrencyFunctions()
    for cart_price_type, cart_price_value in cart_prices.items():
        try:
            data_store_price = data_store.scenario['prices'][cart_price_type]

            logger.info(f"Comparing the price from store {data_store_price} "
                        f"with the price from cart {cart_price_value}")

            assert currency_function.check_same_currency(cart_price_value, data_store_price), \
                f"Failed to match the currency for product in cart for {cart_price_type}." \
                f"\nExpected results: {cart_price_value}" \
                f"\nActual results: {data_store_price}"

            cart_price_value = currency_function.remove_price_currency(cart_price_value)
            data_store_price = currency_function.remove_price_currency(data_store_price)

            assert cart_price_value == data_store_price, \
                f"Failed to match the price for product in cart for {cart_price_type}." \
                f"\nExpected results: {cart_price_value}" \
                f"\nActual results: {data_store_price}"

        except KeyError as e:
            raise KeyError(f"Failed to find the expected key in data_store dictionary: {repr(e)}")

    logger.info("The correct price and product has been displayed in cart")


@step("Verify if the webpage has returned to product page")
def verify_session_in_product_page():
    assert Driver.driver.check_exists(Solutions.MULTIPLATFORM), "Failed to load \'Solutions\' page"
    logger.info("\'Solutions\' page has been loaded correctly, the product has been removed from cart.")
