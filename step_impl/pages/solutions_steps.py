from getgauge.python import step
from core_elements.pages.solutions_page import Solutions
from core_elements.logging_element import logger


@step("Find and click Multiplatform")
def find_and_click_multiplatform():
    solutions_page = Solutions()
    solutions_page.click_multiplaform()


@step("Click on buy product <product>")
def click_on_buy_product(product):
    solutions_page = Solutions()
    logger.info(f"Buying product {product}")
    solutions_page.click_cumpara_premium_security()
    import pdb; pdb.set_trace()


@step("Verify if <text_to_verify> is selected for multiplatform")
def verify_text_is_selected(text_to_verify):
    solutions_page = Solutions()
    premium_security = solutions_page.premium_security
    assert premium_security.text == text_to_verify, f"Failed to find the selected text: {text_to_verify}. " \
                                                    f"Found {premium_security.text}"
    logger.info(f"{premium_security.text} has been selected")

    logger.info(f"Storing the price for {text_to_verify}")
    prices = solutions_page.get_price_information()
    import pdb; pdb.set_trace()

@step("Verify the correct price has been displayed in cart")
def verify_correct_price():
    pass