import unittest
import datetime
from ..stock import Stock

class StockTest(unittest.TestCase):
    def test_price_of_a_new_stock_class_should_be_None(self):
        stock = Stock("GOOG")
        self.assertIsNone(stock.price)
    
    def test_stock_update(self):
        goog = Stock("GOOG")
        goog.update(datetime(2021,3,16),price=10)
        self.assertEqual(10,goog.price)