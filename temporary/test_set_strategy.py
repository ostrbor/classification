# import unittest
# from strategies import SetStrategy
# from db_api import GroupRelation

# derivative category is letter uppercase
# base category is letter lowercase


# class SetStrategyTest(unittest.TestCase):
#     def setUp(self):
#         self.data = None
#         self.strategy = SetStrategy(self.data)
#
#     def test_get_unique_base_subgroups(self):
#         data = {'a': 1, 'b': 2}
#         expected = ['a']
#         actual = self.strategy.get_unique_base_subgroups(data)
#         self.assertEqual(expected, list(actual))
#
#     def test_get_intersection(self):
#         expected = GroupRelation(base='a', derivative=None)
#         data = [expected, GroupRelation(base='b', derivative=None)]
#         self.strategy.categories = data
#         res = self.strategy.get_intersection(['a'])
#         self.assertEqual([expected], res)
#
#     def test_count_base_subgroups(self):
#         derivative_groups = {'A': ['a', 'b', 'a', 'b'], 'B': ['a', 'c']}
#         expected = {'a': 3, 'b': 2, 'c': 1}
#         self.assertDictEqual(
#             expected, self.strategy.count_base_subgroups(derivative_groups))
#
#     def test_group_derivative_categories(self):
#         cat1 = GroupRelation(base='a', derivative='A')
#         cat2 = GroupRelation(base='b', derivative='A')
#         cat3 = GroupRelation(base='a', derivative='B')
#         data = [cat1, cat2, cat3]
#
#         self.strategy.categories = data
#         expected = {'A': ['a', 'b'], 'B': ['a']}
#         self.assertDictEqual(expected,
#                              self.strategy.group_derivative_categories())
#
#     def test_get_unreliable_categories(self):
#         data = ['a', 'b', 'c']
#         reliable = ['a']
#         self.strategy.categories = data
#         self.strategy.reliable_categories = reliable
#         expected = ['b', 'c']
#         self.assertEqual(expected, self.strategy.get_unreliable_categories())
#
#     def test_count_derivatives(self):
#         data = ['a', 'b', 'a']
#         expected = {'a': 2, 'b': 1}
#         self.assertDictEqual(expected, self.strategy.count_derivatives(data))
#
#     def test_filter_by_threshold(self):
#         data = {'a': 100}
#         self.assertEqual(('a', 100), self.strategy.filter_by_threshold(data))
#
#         data = {'a': 1, 'b': 1}
#         self.assertEqual((None, None), self.strategy.filter_by_threshold(data))
#
#         data = {'a': 9, 'b': 1}
#         self.assertEqual(('a', 90), self.strategy.filter_by_threshold(data))
