from enum import Enum


class SortBy(str, Enum):
    ASCENDING = 'ascending'
    DESCENDING = 'descending'