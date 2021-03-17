import unittest
from datetime import date, datetime
from ..stock import Stock

class StockTest(unittest.TestCase):
    def test_price_of_a_new_stock_class_should_be_None(self):
        stock = Stock("GOOG")
        self.assertIsNone(stock.price)
    
    def test_stock_update(self):
        goog = Stock("GOOG")
        goog.update(datetime(2021,3,16),price=10)
        self.assertEqual(10,goog.price)
    
    def test_negative_price_should_throw_valueError(self):
        goog = Stock("GOOG")
        self.assertRaises(ValueError,goog.update,datetime(2021,3,16),-1)

    def test_stock_price_should_give_the_latest_price(self):
        goog = Stock("GOOG")
        goog.update(datetime(2021,3,17),price=10)
        goog.update(datetime(2021,3,17),price=8.4)
        self.assertAlmostEqual(8.4, goog.price,delta=0.0001)