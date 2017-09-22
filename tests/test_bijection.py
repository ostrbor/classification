import unittest
from strategies import Bijection
from db_api import GroupRelation
from group_relations import GroupRelation

# derivative category is letter uppercase
# base category is letter lowercase

class BijectionTest(unittest.TestCase):
    def setUp(self):
        self.strategy = Bijection([])

    def test_get_unique_base_subgroups(self):
        data = {'a': 1, 'b': 2}
        expected = ['a']
        actual = self.strategy.get_unique_base_subgroups(data)
        self.assertEqual(expected, list(actual))

    def test_get_bijective_groups(self):
        expected = GroupRelation('a', None)
        data = [expected, GroupRelation('b', None)]
        self.strategy.group_relations = data
        res = self.strategy.get_bijective_groups(['a'])
        self.assertEqual([expected], res)

    def test_count_base_subgroups(self):
        derivative_groups = {'A': ['a', 'b', 'a', 'b'], 'B': ['a', 'c']}
        expected = {'a': 3, 'b': 2, 'c': 1}
        self.assertDictEqual(
            expected, self.strategy.count_base_subgroups(derivative_groups))

    def test_group_derivatives(self):
        cat1 = GroupRelation('a', 'A')
        cat2 = GroupRelation('b', 'A')
        cat3 = GroupRelation('a', 'B')
        data = [cat1, cat2, cat3]

        self.strategy.group_relations = data
        expected = {'A': ['a', 'b'], 'B': ['a']}
        self.assertDictEqual(expected,
                             self.strategy.group_derivatives())
