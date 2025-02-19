from abc import ABC, abstractmethod
from typing import Any, Dict, Optional

class BaseDataSource(ABC):
    @abstractmethod
    def connect(self, config: Dict[str, Any]) -> bool:
        """Initialize connection to data source"""
        pass

    @abstractmethod
    def load_data(self, **kwargs) -> Any:
        """Load data from source"""
        pass

    @abstractmethod
    def validate_connection(self) -> bool:
        """Validate connection is active"""
        pass