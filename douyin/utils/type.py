from enum import Enum, unique

@unique
class AppType(Enum):
    SELF = 'SELF'
    TOOL = 'TOOL'