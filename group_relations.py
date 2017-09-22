from collections import namedtuple
from typing import List, Dict, Tuple

GroupRelation = namedtuple('GroupRelation', ['base_group', 'derivative_group'])


class GroupRelations:
    """
    Data object: list of tuples where first value is base group,
    second value is derivative group.
    """
    def __init__(self, data):
        self.data = self.convert(data)

    def convert(self, data: List[Tuple]) -> List[namedtuple]:
        return [GroupRelation(*x) for x in data]
