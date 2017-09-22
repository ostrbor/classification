from typing import List, Dict, Tuple

from temporary.bijection_mixin import BijectionMixin
from temporary.probability_mixin import ProbabilityMixin

Groups = Dict[str, List[str]]


class SetStrategy(BijectionMixin, ProbabilityMixin):
    categories = None
    reliable_categories = None
    unreliable_to_save = None
    unreliable_categories = None  # (base, derivative, probability)

    def __init__(self, data):
        self.categories = data

    def process(self):
        self.bijective_function()
        self.probability_function()

    def bijective_function(self) -> List[Tuple]:
        grouped_derivatives = self.group_derivative_categories()
        counted_bases = self.count_base_subgroups(grouped_derivatives)
        unique_bases = self.get_unique_base_subgroups(counted_bases)
        self.reliable_categories = self.get_intersection(unique_bases)
        self.save_reliable_categories()

    def probability_function(self):
        self.unreliable_to_save = self.get_unreliable_categories()
        grouped_bases = self.group_base_categories(self.unreliable_to_save)
        self.unreliable_categories = self.filter_unreliable_categories(
            grouped_bases)
        self.save_unreliable_categories()
