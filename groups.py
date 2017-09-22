from collections import namedtuple
from typing import List, Dict, Tuple

Group = namedtuple('Group', ['base', 'derivative'])


class Groups:
    """
    Data object. Input must follow protocol: list of tuples where first value is base,
    second value is derivative.
    """
    def __init__(self, data):
        self.data = self.convert(data)

    def convert(self, data: List[Tuple]) -> List[namedtuple]:
        return [Group(*x) for x in data]
