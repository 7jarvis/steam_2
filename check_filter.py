class CheckFilter:
    @staticmethod
    def is_filtering_working(prices):
        check_prices = []
        num_prices = []
        for value in prices:
            check_prices.append(value)
        for item in prices:
            value = item.split()
            for number in value:
                try:
                    number = float(number)
                    num_prices.append(number)
                except ValueError:
                    pass

        sorted_prices = sorted(num_prices, reverse=True)
        return num_prices == sorted_prices
