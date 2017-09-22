from typing import List, Dict, Tuple
from collections import defaultdict
from models import Prediction

Groups = Dict[str, List[str]]


class BijectionMixin:
    def group_derivative_categories(self) -> Groups:
        res = defaultdict(list)
        for cat in self.categories:
            res[cat.derivative].append(cat.base)
        return res

    def count_base_subgroups(self, groups: Groups) -> Dict[str, int]:
        res = defaultdict(int)
        for group, subgroups in groups.items():
            for subgroup in subgroups:
                res[subgroup] += 1
        return res

    def get_unique_base_subgroups(
            self, counted_subrgoups: Dict[str, int]) -> List[str]:
        return list(
            filter(lambda x: counted_subrgoups[x] == 1, counted_subrgoups))

    def get_intersection(self, unique_bases: List[str]) -> List[Tuple]:
        res = []
        for entry in self.categories:
            if entry.base in unique_bases:
                res.append(entry)
        return res

    def save_reliable_categories(self):
        for cat in self.reliable_categories:
            record = Prediction(
                category=cat.base,
                eshop_category=cat.derivative,
                set_probability=100)
            record.save()

    def get_unreliable_categories(self) -> List:
        res = []
        for cat in self.categories:
            if cat not in self.reliable_categories:
                res.append(cat)
        return res
