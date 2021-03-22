class Event:
    def __init__(self) :
        self.listeners=[]
        
    def connect(self,listener):
        self.listeners.append(listener)

    def fire (self,*args,**kwargs):
        for listener in self.listeners:
            listener(*args,**kwargs)

class Mock:
    def __init__(self):
        self.called = False
        self.params = ()
    
    def __call__(self, *args, **kwds):
        self.called=True
        self.params = (args,kwds)