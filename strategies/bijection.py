from typing import List, Dict
from collections import defaultdict
from group_relations import GroupRelation, GroupRelations


class Bijection:
    """
    To find one to one relationship between two fields in Groups: base and derivative.
    Result: table where it's possible to predict derivative value by base value.
    """
    categories = None
    reliable_categories = None
    unreliable_to_save = None
    unreliable_categories = None  # (base, derivative, probability)

    def __init__(self, group_relations: GroupRelations):
        self.group_relations = group_relations

    def process(self) -> GroupRelations:
        grouped_dervs = self.group_derivatives()
        counted_bases = self.count_base_subgroups(grouped_dervs)
        unique_bases = self.get_unique_base_subgroups(counted_bases)
        bijective_groups = self.get_bijective_groups(unique_bases)
        return GroupRelations(bijective_groups)

    def group_derivatives(self) -> Dict[str, List[str]]:
        res = defaultdict(list)
        for group_relation in self.group_relations:
            res[group_relation.derivative_group].append(group_relation.base_group)
        return res

    def count_base_subgroups(self, grouped_dervs: Dict[str, List[str]]) -> Dict[str, int]:
        ANOTHER_ONE = 1
        res = defaultdict(int)
        for group, subgroups in grouped_dervs.items():
            for subgroup in subgroups:
                res[subgroup] += ANOTHER_ONE
        return res

    def get_unique_base_subgroups(self, counted_bases: Dict[str, int]) -> List[str]:
        ONLY_ONCE = 1
        return list(filter(lambda x: counted_bases[x] == ONLY_ONCE, counted_bases))

    def get_bijective_groups(self, unique_bases: List[str]) -> List[GroupRelation]:
        res = []
        for group_relation in self.group_relations:
            if group_relation.base_group in unique_bases:
                res.append(group_relation)
        return res
