from datetime import datetime

class ListReader:
    def __init__(self,updates):
        self.updates = updates
        
    def get_updates(self):
        for update in self.updates:
            yield update