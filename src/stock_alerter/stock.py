import bisect
import collections
from enum import Enum
from datetime import timedelta
from stock_alerter.timeseries import TimeSeries

PriceEvent = collections.namedtuple("PriceEvent", ["timestamp", "price"])


class Stock:
    LONG_TERM_TIMESPAN = 10
    SHORT_TERM_TIMESPAN = 5

    def __init__(self, symbol):
        self.symbol = symbol
        self.price_history = []
        self.history = TimeSeries()

    def update(self, timestamp, price):
        if price < 0:
            raise ValueError("price should not be negative")

        bisect.insort_left(self.price_history, PriceEvent(timestamp, price))

        self.history.update(timestamp,price)

    def is_increasing_trend(self):
        return self.history[-3].value < self.history[-2].value < self.history[-1].value

    def get_crossover_signal(self, on_date):

        NUM_DAYS = self.LONG_TERM_TIMESPAN + 1
        closing_price_list = self.history._get_closing_price_list(on_date= on_date,num_days= NUM_DAYS)
        # Return NEUTRAL signal
        if len(closing_price_list) < NUM_DAYS:
            return StockSignal.neutral

        long_term_series=closing_price_list[-self.LONG_TERM_TIMESPAN:]
        prev_long_term_series= closing_price_list[-self.LONG_TERM_TIMESPAN-1:-1]

        short_term_series=closing_price_list[-self.SHORT_TERM_TIMESPAN:]
        prev_short_term_series=closing_price_list[-self.SHORT_TERM_TIMESPAN-1:-1]

        long_term_ma = sum([update.price for update in long_term_series]) /self.LONG_TERM_TIMESPAN
        prev_long_term_ma= sum([update.price for update in prev_long_term_series])/self.LONG_TERM_TIMESPAN

        short_term_ma = sum([update.price for update in short_term_series])/self.SHORT_TERM_TIMESPAN
        prev_short_term_ma= sum([update.price for update in prev_short_term_series])/self.SHORT_TERM_TIMESPAN
        #   BUY signal
        if self._is_crossover_below_to_above(prev_ma=prev_short_term_ma,prev_reference_ma=prev_long_term_ma,current_ma=short_term_ma,current_reference_ma=long_term_ma):
            return StockSignal.buy
        
        #   SELL signal
        
        if self._is_crossover_above_to_blow(prev_ma=prev_long_term_ma,prev_reference_ma=prev_short_term_ma,current_ma=long_term_ma,current_reference_ma=short_term_ma):
            return StockSignal.sell
        
        # NEUTRAL signal
        return StockSignal.neutral
    def _is_crossover_below_to_above(self,prev_ma,prev_reference_ma,current_ma,current_reference_ma):
        return prev_ma < prev_reference_ma and current_ma > current_reference_ma

    def _is_crossover_above_to_blow(self,prev_ma,prev_reference_ma,current_ma,current_reference_ma):
        return prev_ma > prev_reference_ma and current_ma < current_reference_ma

    
    @property
    def price(self):
        try:
            return self.history[-1].value
        except IndexError:
            return None
class StockSignal(Enum):
    buy = 1
    neutral = 0
    sell =-1
