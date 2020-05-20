from typing import List, Optional, TypeVar

_T = TypeVar('_T')

def filter_nulls(ts: List[Optional[_T]]) -> List[_T]:
    return [t for t in ts if t is not None]
