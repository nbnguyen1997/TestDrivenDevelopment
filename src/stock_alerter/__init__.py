r"""
The stock_alerter module allows you to set up rules and get alerted
when those rules are met.

>>> from datetime import datetime
>>> from stock_alerter.stock import Stock
>>> exchange={"GOOG":Stock("GOOG"), "AAPL":Stock("AAPL")}
>>> from stock_alerter.reader import ListReader
>>> reader = ListReader([("GOOG",datetime(2014,2,8),5)])
>>> from stock_alerter.alert import Alert
>>> from stock_alerter.rule import PriceRule
>>> from stock_alerter.action import PrintAction
>>> alert = Alert("GOOG > $3", PriceRule("GOOG",lambda s:s.price > 3), \
...             PrintAction())
>>> alert.connect(exchange)
>>> from stock_alerter.processor import Processor
>>> processor = Processor(reader, exchange)
>>> processor.process()
GOOG > $3
"""

if __name__== "__main__":
    import doctest
    doctest.testmod()