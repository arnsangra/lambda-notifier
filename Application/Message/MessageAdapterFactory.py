"""a"""
class MessageAdapterFactory:

    def __init__(self):
        #discover adapters
        self.adapters = None
    
    def getAdapter(self, name):
       adapter = list(filter(lambda a: a.canHandle(name) ,self.adapters))
       try:
           return adapter[0]
       except IndexError:
           return None
               