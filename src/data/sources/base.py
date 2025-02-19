# Abstract base class for data sources
from abc import ABC, abstractmethod

class BaseDataSource(ABC):
    @abstractmethod
    def connect(self):
        pass
    
    @abstractmethod
    def load_data(self):
        pass