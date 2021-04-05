import unittest
from stock_alerter.tests.test_stock import StockCrossOverSignalTest
def suite():
    loader = unittest.TestLoader()
    test_suite = unittest.TestSuite()
    test_suite.addTest(
        loader.loadTestsFromTestCase(StockCrossOverSignalTest)
    )
    return test_suite


if __name__== "__main__":
    suite()