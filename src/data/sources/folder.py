from typing import Any, Dict
from .base import BaseDataSource
import pandas as pd

class FolderDataSource(BaseDataSource):
    def __init__(self):
        self.base_path = None

    def connect(self, config: Dict[str, Any]) -> bool:
        self.base_path = config.get('path')
        return self.base_path is not None

    def load_data(self, filename: str, **kwargs) -> pd.DataFrame:
        return pd.read_csv(f"{self.base_path}/{filename}")

    def validate_connection(self) -> bool:
        return self.base_path is not None