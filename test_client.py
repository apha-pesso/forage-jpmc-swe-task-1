import unittest
from client3 import getDataPoint, getRatio

# self.assertEqual(stock, quote['stock'])
# self.assertEqual(bid_price, quote['top_bid']['price'])
# self.assertEqual(ask_price, quote['top_ask']['price'])
# quote_price = (quote['top_bid']['price'] + quote['top_ask']['price']) / 2
# quote_price = round(quote_price, 2)
# self.assertEqual(price, quote_price)


class ClientTest(unittest.TestCase):
    def test_getDataPoint_calculatePrice(self):
        quotes = [{'top_ask': {'price': 121.2,
                               'size': 36},
                   'timestamp': '2019-02-11 22:06:30.572453',
                   'top_bid': {'price': 120.48,
                                'size': 109},
                   'id': '0.109974697771',
                   'stock': 'ABC'},
                  {'top_ask': {'price': 121.68,
                               'size': 4},
                   'timestamp': '2019-02-11 22:06:30.572453',
                   'top_bid': {'price': 117.87,
                               'size': 81},
                   'id': '0.109974697771',
                   'stock': 'DEF'}]
        """ ------------ Add the assertion below ------------ """
        for quote in quotes:
            stock, bid_price, ask_price, price = getDataPoint(quote)
            quote_price = (quote['top_bid']['price'] +
                           quote['top_ask']['price']) / 2
            quote_price = round(quote_price, 2)
            self.assertEqual(price, quote_price)

    def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
        quotes = [{'top_ask': {'price': 119.2,
                               'size': 36},
                   'timestamp': '2019-02-11 22:06:30.572453',
                   'top_bid': {'price': 120.48,
                                'size': 109},
                   'id': '0.109974697771',
                   'stock': 'ABC'},
                  {'top_ask': {'price': 121.68,
                               'size': 4},
                   'timestamp': '2019-02-11 22:06:30.572453',
                   'top_bid': {'price': 117.87,
                               'size': 81},
                   'id': '0.109974697771',
                   'stock': 'DEF'}]
        """ ------------ Add the assertion below ------------ """
        for quote in quotes:
            stock, bid_price, ask_price, price = getDataPoint(quote)
            quote_price = (quote['top_bid']['price'] +
                           quote['top_ask']['price']) / 2
            quote_price = round(quote_price, 2)
            self.assertEqual(price, quote_price)

    def test_getDataPoint_calculatePriceBidLessThanAsk(self):
        quotes = [{'top_ask': {'price': 121.2,
                               'size': 36},
                   'timestamp': '2019-02-11 22:06:30.572453',
                   'top_bid': {'price': 119.48,
                                'size': 109},
                   'id': '0.109974697771',
                   'stock': 'ABC'},
                  {'top_ask': {'price': 121.68,
                               'size': 4},
                   'timestamp': '2019-02-11 22:06:30.572453',
                   'top_bid': {'price': 117.87,
                               'size': 81},
                   'id': '0.109974697771',
                   'stock': 'DEF'}]
        """ ------------ Add the assertion below ------------ """
        for quote in quotes:
            stock, bid_price, ask_price, price = getDataPoint(quote)
            quote_price = (quote['top_bid']['price'] +
                           quote['top_ask']['price']) / 2
            quote_price = round(quote_price, 2)
            self.assertEqual(price, quote_price)

    def test_getRatio_calculateRatio(self):
        price_a = 119.2
        price_b = 121.2

        ratio = getRatio(price_a, price_b)
        ratio = round(ratio, 2)
        self.assertEqual(ratio, 0.98)


if __name__ == '__main__':
    unittest.main(verbosity=2)
