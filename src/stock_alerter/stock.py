import bisect
import collections
from enum import Enum
from datetime import timedelta
PriceEvent = collections.namedtuple("PriceEvent", ["timestamp", "price"])


class Stock:
    LONG_TERM_TIMESPAN = 10
    SHORT_TERM_TIMESPAN = 5

    def __init__(self, symbol):
        self.symbol = symbol
        self.price_history = []

    def update(self, timestamp, price):
        if price < 0:
            raise ValueError("price should not be negative")

        bisect.insort_left(self.price_history, PriceEvent(timestamp, price))

    def is_increasing_trend(self):
        return self.price_history[-3].price < self.price_history[-2][1] < self.price_history[-1][1]

    def get_crossover_signal(self, on_date):

        NUM_DAYS = self.LONG_TERM_TIMESPAN + 1
        closing_price_list = self._get_closing_price_list(on_date= on_date,num_days= NUM_DAYS)
        # Return NEUTRAL signal
        if len(closing_price_list) < 11:
            return 0

        #   BUY signal
        if sum([update.price for update in closing_price_list[-11:-1]])/10 > sum([update.price for update in closing_price_list[-6, -1]])/5 and sum([update.price for update in closing_price_list[-10:]])/10 < sum([update.price for update in closing_price_list[-5:]])/5:
            return StockSignal.buy

        #   SELL signal
        if sum([update.price for update in closing_price_list[-11:-1]])/10 < sum([update.price for update in closing_price_list[-6, -1]])/5 and sum([update.price for update in closing_price_list[-10:]])/10 > sum([update.price for update in closing_price_list[-5:]])/5:
            return StockSignal.sell
        # NEUTRAL signal
        return StockSignal.neutral
    def _get_closing_price_list(self,on_date,num_days):
        closing_price_list=[]
        for i in range(num_days):
            chk = on_date.date() - timedelta(i)
            for price_event in reversed(self.price_history):
                if price_event.timestamp.date()>chk:
                    pass
                if price_event.timestamp.date() == chk:
                    closing_price_list.insert(0,price_event)
                    break
                if price_event.timestamp.date()<chk:
                    closing_price_list.insert(0,price_event)
        
        return closing_price_list
    @property
    def price(self):
        return self.price_history[-1].price if self.price_history else None

class StockSignal(Enum):
    buy = 1
    neutral = 0
    sell =-1
