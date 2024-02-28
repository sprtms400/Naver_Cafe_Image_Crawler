from enum import Enum
from datetime import datetime

class nodeType(Enum):
    GALLERY = 'gallery'
    SHOWROOM = 'showroom'
    ARTWORK = 'artwork'
    ROOT = 'root'
    
class nodeData:
    nodeId: str
    type: nodeType
    url: str
    isConquered: bool
    conqueredDate: datetime