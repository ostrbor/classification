from collections import namedtuple
from typing import List, Dict, Tuple, Union
from models import Prediction

GroupRelation = namedtuple('GroupRelation', ['base_group', 'derivative_group',
                                             'base_group_name', 'derivative_group_name',
                                             'ngram_probability'])
GroupRelation.__new__.__defaults__ = (None,) * len(GroupRelation._fields)


class GroupRelations:
    """
    Data object: list of tuples where first value is base group,
    second value is derivative group.
    """

    def __init__(self, data):
        self.data = self._convert(data)

    def __iter__(self):
        self.counter = 0
        return self

    def __next__(self) -> GroupRelation:
        if self.counter == len(self.data):
            raise StopIteration
        next_value = self.data[self.counter]
        self.counter += 1
        return next_value

    def __sub__(self, other):
        """
        To find GroupRelations in self that are not present in other
        """
        res = []
        for group_relation in self.data:
            if group_relation not in other.data:
                res.append(group_relation)
        return GroupRelations(res)

    def __len__(self):
        return len(self.data)

    def _convert(self, data) -> List[namedtuple]:
        # data input: List[Tuples] or GroupRelations
        # needs to be converted if List[Tuples]
        return [GroupRelation(*x) for x in data]

    def save_bijection_results(self):
        for group_relation in self.data:
            record = Prediction(category=group_relation.base_group,
                                eshop_category=group_relation.derivative_group,
                                set_probability=100)
            record.save()

    def save_ngram_results(self):
        for group_relation in self.data:
            probability = int(group_relation.ngram_probability*100)
            record = Prediction(category=group_relation.base_group,
                                eshop_category=group_relation.derivative_group,
                                ngram_probability=probability)
            record.save()
