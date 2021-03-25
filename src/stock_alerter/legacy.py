from datetime import datetime
import stock
# from .rule import PriceRule
import rule


class AlertProcessor:
    def __init__(self):
        self.exchange = {"GOOG": sotck.Stock("GOOG"),
                         "AAPL": stock.Stock("AAPL")}
        rule_1 = rule.PriceRule("GOOG", lambda stock: stock.price > 10)
        rule_2 = rule.PriceRule("AAPL", lambda stock: stock.price > 5)
        # self.exchange["GOOG"].update.connect(
        #     lambda stock: print(stock.symbol, stock.price)
        #     if rule_1.matches(self.exchange) else None)
        # self.exchange["AAPL"].update.connect(
        #     lambda stock: print(stock.symbol, stock.price)
        #     if rule_2.matches(self.exchange) else None)

        updates = []
        
        with open(r".\updates.csv", "r") as fp:
            for line in fp.readline():
                symbol, timestamp, price = line.strip().split(',')
                updates.append((symbol, datetime.strptime(
                    timestamp, "%Y-%m-%dT%H:%m:%S.%f"), int(price)))

        for symbol, timestamp, price in updates:
            stock = self.exchange[symbol]
            stock.update(timestamp, price)
