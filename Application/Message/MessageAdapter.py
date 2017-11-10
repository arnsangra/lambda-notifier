"""a"""

from abc import ABC, abstractmethod

class MessageAdapter(ABC):
    """a"""

    def __init__(self, name):
        self.name = name

    def canHandle(self, name):
        """a"""
        return self.name == name

    @abstractmethod
    def adapt(self, message):
        """a"""
        pass


class DataPipelineMessageAdapter(MessageAdapter):
    """a"""

    name = "DataPipeline"

    def __init__(self):
        MessageAdapter.__init__(self, "DataPipeline")
    
    def adapt(self, message):
        return message