from collections import namedtuple
from typing import List, Dict, Tuple, Union
from models import Prediction

GroupRelation = namedtuple('GroupRelation', ['base_group', 'derivative_group'])


class GroupRelations:
    """
    Data object: list of tuples where first value is base group,
    second value is derivative group.
    """

    def __init__(self, data):
        self.data = self.convert(data)

    def convert(self, data) -> List[namedtuple]:
        # data: List[Tuples] or GroupRelations
        return [GroupRelation(*x) for x in data]

    def save_results(self):
        for group_relation in self.data:
            record = Prediction(category=group_relation.base_group,
                                eshop_category=group_relation.derivative_group,
                                set_probability=100)
            record.save()

    def __sub__(self, other):
        """
        To find GroupRelations in self that are not present in other
        """
        res = []
        for group_relation in self.data:
            if group_relation not in other.data:
                res.append(group_relation)
        return GroupRelations(res)
