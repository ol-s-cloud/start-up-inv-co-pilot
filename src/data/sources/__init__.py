from enum import Enum

class DataSourceType(Enum):
    FOLDER = 'folder'
    DATALAKE = 'datalake'
    API = 'api'
    DEMO = 'demo'