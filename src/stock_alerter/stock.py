import bisect
class Stock:
    def __init__(self,symbol):
        self.symbol = symbol
        self.price_history = []
        self.timestamp_history=[]

    def update(self, timestamp, price):
        if price < 0:
            raise ValueError("price should not be negative")
        
        self.timestamp_history.append(timestamp)
        self.price_history.append(price)
    
    def is_increasing_trend(self):
        return self.price_history[-3]<self.price_history[-2] < self.price_history[-1]

    @property
    def price(self):
        if self.price_history :
            list_temp = self.timestamp_history[::-1]
            max_time = max(list_temp)

            return self.price_history[len(list_temp)-1-list_temp.index(max_time)]
        else :
            return None

