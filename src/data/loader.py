from typing import Dict, Any
from .sources import DataSourceType
from .sources.base import BaseDataSource
from .sources.folder import FolderDataSource
from .sources.datalake import DataLakeSource
from .sources.api import APIDataSource

class DataLoader:
    def __init__(self, source_type: DataSourceType):
        self.source_type = source_type
        self.source: BaseDataSource = self._initialize_source()

    def _initialize_source(self) -> BaseDataSource:
        if self.source_type == DataSourceType.FOLDER:
            return FolderDataSource()
        elif self.source_type == DataSourceType.DATALAKE:
            return DataLakeSource()
        elif self.source_type == DataSourceType.API:
            return APIDataSource()
        else:
            raise ValueError(f"Unsupported source type: {self.source_type}")

    def connect(self, config: Dict[str, Any]) -> bool:
        return self.source.connect(config)

    def load_data(self, **kwargs) -> Any:
        return self.source.load_data(**kwargs)