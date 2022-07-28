from core_elements.logging_element import logger


def check_same_currency(*args):
    ron_currency = ('RON', 'LEI', 'LEU', 'ron', 'lei', 'leu')
    logger.info(f"Checking the same currency for {args}")

    import pdb;
    pdb.set_trace()
    for i in range(len(args)):
        condition = any(currency in args[i] for currency in ron_currency)
        if condition:
            pass
    return False
