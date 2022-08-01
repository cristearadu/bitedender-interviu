import re


class CurrencyFunctions:
    """
    Class for currency operations
    """

    # ~ What can be improved ~ create a custom class for price objects with specific parameters for currency
    # Class PriceObject('$')
    # Then for each currency type use the functions below and automate the parsing mechanism

    RON_CURRENCY = ('RON', 'LEI', 'LEU', 'ron', 'lei', 'leu')
    # pentru euro si dolari am cautat pe bitdefender.fr si bitdefender.com
    EURO_CURRENCY = ('€', 'EUR')
    DOLAR_CURRENCY = ('$', 'USD')
    LIST_OF_ALL_CURRENCIES = [RON_CURRENCY, EURO_CURRENCY, DOLAR_CURRENCY]

    CURRENCY_REGEX = fr"({'|'.join(DOLAR_CURRENCY)})?" + \
                     fr"(\d*(\.|\,)\d*)\ *" + \
                     fr"(({'|'.join(RON_CURRENCY)})\|" + \
                     fr"({'|'.join(EURO_CURRENCY)}))?"
    DISCOUNT_REGEX = r'(\d*)\%\ reducere'

    def check_same_currency(self, price_1, price_2):
        """
        Function that checks the same currency for two prices.
        """

        # ~ What can be improved ~ add *args as a parameter

        for currency_list in self.LIST_OF_ALL_CURRENCIES:
            if any(currency in price_1 for currency in currency_list) and any(
                    currency in price_2 for currency in currency_list):
                return True

    def remove_price_currency(self, price):
        """
        Function that removes price currency from total price
        """

        # Could have done eat a lot easier, using string.split() function, by whitespace or by other symbols (for $)

        match = re.search(self.CURRENCY_REGEX, price)
        if match:
            try:
                return int(match.group(2).replace(',', '.'))
            except ValueError:
                return float(match.group(2).replace(',', '.'))


"""
# Testing purpose for 

for el in ['669,99 RON', '289,99 RON', '289.99 LEI', '669.99 LEI', '58.77 €', '135.78 €']:
    assert CurrencyFunctions().remove_price_currency(el)
"""