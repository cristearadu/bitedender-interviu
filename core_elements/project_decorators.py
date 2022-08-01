from core_elements.logging_element import logger


def log_click_button(function_click):
    """
    Wrapper used for logging the action of clicking a button inside a class.
    Reason is to be specific on which button is clicked
    """
    def wrapper(*args, **kwargs):
        function_name = str(function_click.__name__)
        function_name = function_name.replace('click_', '')
        logger.info(f"Clicking on {function_name}")
        return function_click(*args, **kwargs)
    return wrapper


def log_attribute_and_value(function_name):
    """
    Wrapper used for logging inside a textbox. Reason is to be specific on which textbox is the user is writing
    and what information is passed on.
    """
    def wrapper(*args, **kwargs):
        logger.info(f"Selecting {function_name.__name__}: {args[1]}")
        return function_name(*args, **kwargs)
    return wrapper
