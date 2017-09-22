from collections import defaultdict
from typing import List, Dict, Tuple
from models import Prediction

PROBABILITY_THRESHOLD = 80


class ProbabilityMixin:
    def get_unreliable_categories(self) -> List:
        res = []
        for cat in self.categories:
            if cat not in self.reliable_categories:
                res.append(cat)
        return res

    def group_base_categories(self, unreliable) -> Dict[str, List]:
        res = defaultdict(list)
        for cat in unreliable:
            res[cat.base].append(cat.derivative)
        return res

    def filter_unreliable_categories(self, grouped_bases):
        res = []
        for base, derivatives in grouped_bases.items():
            counted_der = self.count_derivatives(derivatives)
            derivative, probability = self.filter_by_threshold(counted_der)
            if derivative:
                res.append((base, derivative, probability))
        return res

    def count_derivatives(self, derivatives: List) -> Dict:
        res = defaultdict(int)
        for cat in derivatives:
            res[cat] += 1
        return res

    def filter_by_threshold(self, counted_derivatives: Dict) -> str:
        total_count = sum(counted_derivatives.values())
        max_counted = max(counted_derivatives, key=counted_derivatives.get)
        probability = int(counted_derivatives[max_counted] / total_count * 100)
        if probability >= PROBABILITY_THRESHOLD:
            return max_counted, probability
        else:
            return None, None

    def save_unreliable_categories(self):
        for cat in self.unreliable_categories:
            record = Prediction(
                category=cat[0], eshop_category=[1], set_probability=[2])
            record.save()
