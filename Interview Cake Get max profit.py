def get_max_profit(stock_prices):

    # Calculate the max profit
    # if len(stock_prices) < 2:
    #     return 0
    
    _max = stock_prices[1] - stock_prices[0]
    lows = stock_prices[0]
    
    for index in range(1, len(stock_prices)):
        _max = max(stock_prices[index] - lows,  _max)
        lows = min(stock_prices[index], lows)
    return _max
    
    
    # _max = stock_prices[1] - stock_prices[0]
    # lows = [stock_prices[0]]
    
    # for index in range(1, len(stock_prices)):
    #     if stock_prices[index] < lows[index - 1]:
    #         lows.append(stock_prices[index])
    #     else:
    #         lows.append(lows[index-1])
        
    #     _max = max(stock_prices[index] - lows[index-1], _max)
            
    # return _max















# Tests

import unittest

class Test(unittest.TestCase):

    def test_price_goes_up_then_down(self):
        actual = get_max_profit([1, 5, 3, 2])
        expected = 4
        self.assertEqual(actual, expected)

    def test_price_goes_down_then_up(self):
        actual = get_max_profit([7, 2, 8, 9])
        expected = 7
        self.assertEqual(actual, expected)

    def test_big_increase_then_small_increase(self):
        actual = get_max_profit([2, 10, 1, 4])
        expected = 8
        self.assertEqual(actual, expected)                

    def test_price_goes_up_all_day(self):
        actual = get_max_profit([1, 6, 7, 9])
        expected = 8
        self.assertEqual(actual, expected)

    def test_price_goes_down_all_day(self):
        actual = get_max_profit([9, 7, 4, 1])
        expected = -2
        self.assertEqual(actual, expected)

    def test_price_stays_the_same_all_day(self):
        actual = get_max_profit([1, 1, 1, 1])
        expected = 0
        self.assertEqual(actual, expected)

    def test_error_with_empty_prices(self):
        with self.assertRaises(Exception):
            get_max_profit([])

    def test_error_with_one_price(self):
        with self.assertRaises(Exception):
            get_max_profit([1])


unittest.main(verbosity=2)
