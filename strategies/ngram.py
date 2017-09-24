from collections import defaultdict
from typing import List, Dict, Tuple

import ngram

from group_relations import GroupRelations, GroupRelation
from settings import NGRAM_PROBABILITY_THRESHOLD, NGRAM_N
from .base import Strategy

NameRelationsType = List[Dict[str, Tuple[str, float]]]


def transform_name(derivative_name):
    lower_case = derivative_name.lower()
    replaced = lower_case.replace(' | ', ' ').replace(' - ', ' ')
    return replaced


class Ngram(Strategy):
    def process(self):
        grouped_bases = self.group_bases()
        self.grouped_categories = grouped_bases
        name_relations = self.apply_ngram(grouped_bases)
        group_relations = self.to_group_relation(name_relations)
        self.result_categories = group_relations
        return group_relations

    def group_bases(self) -> Dict[str, List[str]]:
        res = defaultdict(list)
        for group_relation in self.group_relations:
            res[group_relation.base_group_name].append(group_relation.derivative_group_name)
        return res

    def apply_ngram(self, grouped_bases: Dict[str, List[str]]) -> NameRelationsType:
        MOST_PROBABLE = 0
        res = []
        for base, derivatives_array in grouped_bases.items():
            relation = {}
            G = ngram.NGram(derivatives_array, key=transform_name, threshold=NGRAM_PROBABILITY_THRESHOLD,
                            N=NGRAM_N)
            ngram_result = G.search(base)
            if not ngram_result:
                continue
            else:
                most_suitable = ngram_result[MOST_PROBABLE]
                relation[base] = most_suitable
                res.append(relation)
        return res

    def to_group_relation(self, name_relations: NameRelationsType) -> GroupRelations:
        res = []
        for name_relation in name_relations:
            for base_name, (derivative_name, probability) in name_relation.items():
                old_gr = self.get_group_relation_by_base_name(base_name)
                new_gr = self.build_new_group_relation(old_gr, base_name, derivative_name,
                                                       probability)
                res.append(new_gr)
        return GroupRelations(res)

    def get_group_relation_by_base_name(self, base_name: str):
        ONLY_ONE = 0
        return [x for x in self.group_relations if x.base_group_name == base_name][ONLY_ONE]

    def build_new_group_relation(self, old: GroupRelation,
                                 base_name: str,
                                 derivative_name: str,
                                 probability: float) -> GroupRelation:
        res = GroupRelation(base_group=old.base_group, derivative_group=old.derivative_group,
                            base_group_name=base_name, derivative_group_name=derivative_name,
                            ngram_probability=probability)
        return res
