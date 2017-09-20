from collections import defaultdict, namedtuple
from .db_api import DatabaseApi


class SetApproach:
    def __init__(self, data):
        self.categories = data

    def bijective_function(self):
        grouped_derivatives = self.group_derivative_categories()
        counted_subgroups = self.count_subgroups(grouped_derivatives)
        unique_subgroups = self.get_unique_subgroups(counted_subgroups)

    def group_derivative_categories(self):  # -> Dict
        res = defaultdict(list)
        for cat in self.categories:
            res[cat.derivative].append(cat.base)
        return res

    def filter_unique_subgroups(self, groups):
        res = namedtuple('FilteredResult',
                         ['subgroup', 'group', 'subgroup_count'])
        res = defaultdict(int)
        for group, subgroups in groups.items():
            for subgroup in subgroups:
                res[subgroup] += 1

    def count_subgroups(self, groups):  # -> Dict[str, int]
        res = defaultdict(int)
        for group, subgroups in groups.items():
            for subgroup in subgroups:
                res[subgroup] += 1
        return res

    def get_unique_subgroups(self, counted_subrgoups):
        return filter(lambda x: counted_subrgoups[x] == 1, counted_subrgoups)


class NgramsApproach:
    pass


if __name__ == '__main__':
    api = DatabaseApi()
    data = api.get_distinct_categories_combination()
    import pdb
    pdb.set_trace()
    print('')
