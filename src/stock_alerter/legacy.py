from datetime import datetime
from .stock import Stock
from .rule import PriceRule


class AlertProcessor:
    def __init__(self):
        self.exchange = {"GOOG": Stock("GOOG"),
                         "AAPL": Stock("AAPL")}
        rule_1 = PriceRule("GOOG", lambda stock: stock.price > 10)
        rule_2 = PriceRule("AAPL", lambda stock: stock.price > 5)
        # self.exchange["GOOG"].update.connect(
        #     lambda stock: print(stock.symbol, stock.price)
        #     if rule_1.matches(self.exchange) else None)
        # self.exchange["AAPL"].update.connect(
        #     lambda stock: print(stock.symbol, stock.price)
        #     if rule_2.matches(self.exchange) else None)

        updates = []
        
        with open(r"stock_alerter\updates.csv", "r") as fp:
            for line in fp.readline():
                symbol, timestamp, price = line.strip().split(',')
                updates.append((symbol, datetime.strptime(
                    timestamp, "%Y-%m-%dT%H:%m:%S.%f"), int(price)))

        for symbol, timestamp, price in updates:
            stock = self.exchange[symbol]
            stock.update(timestamp, price)
