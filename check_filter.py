import re


class CheckSorting:
    @staticmethod
    def retrieve_number(price):
        match = re.search(r'\d+[,.]?\d*', price)
        number_str = match.group().replace(',', '.')
        return float(number_str)

    def is_sorting_working(self, prices):
        num_prices = []
        for value in prices.values():
            num_prices.append(self.retrieve_number(value))

        sorted_prices = sorted(num_prices, reverse=True)
        return num_prices == sorted_prices
