import unittest
from datetime import date, datetime
from ..stock import Stock

class StockTest(unittest.TestCase):
    def setUp(self):
        self.goog = Stock("GOOG")

    def test_price_of_a_new_stock_class_should_be_None(self):
        self.assertIsNone(self.goog.price)
    
    def test_stock_update(self):
        self.goog.update(datetime(2021,3,16),price=10)
        self.assertEqual(10,self.goog.price)
    
    def test_negative_price_should_throw_valueError(self):
        self.assertRaises(ValueError,self.goog.update,datetime(2021,3,16),-1)

    def test_stock_price_should_give_the_latest_price(self):        
        self.goog.update(datetime(2021,3,17),price=10)
        self.goog.update(datetime(2021,3,17),price=8.4)
        self.assertAlmostEqual(8.4, self.goog.price,delta=0.0001)

    def test_increasing_trend_is_true_if_price_increase_for_3_updates(self):
        timestamps = [datetime(2021,3,15),datetime(2021,3,16),datetime(2021,3,17)]
        prices=[8,10,12]
        for timestamp,price in zip(timestamps,prices):
            self.goog.update(timestamp,price)
        self.assertTrue(self.goog.is_increasing_trend())

    def test_increasing_trend_is_false_if_price_decreases(self):
        timestamps = [datetime(2014, 2, 11), datetime(2014, 2, 12), \
        datetime(2014, 2, 13)]
        prices = [8, 12, 10]
        for timestamp, price in zip(timestamps, prices):
            self.goog.update(timestamp, price)
        self.assertFalse(self.goog.is_increasing_trend())

    def test_increasing_trend_is_false_if_price_equal(self):
        timestamps = [datetime(2014, 2, 11), datetime(2014, 2, 12), \
        datetime(2014, 2, 13)]
        prices = [8, 10, 10]
        for timestamp, price in zip(timestamps, prices):
            self.goog.update(timestamp, price)
        self.assertFalse(self.goog.is_increasing_trend())