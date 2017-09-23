from unittest import TestCase
from strategies import Ngram
from group_relations import GroupRelations


class NgramTest(TestCase):
    def test_apply_ngram(self):
        strategy = Ngram(GroupRelations([]))
        base_group = 'find these words'
        input_data = {base_group: ['wrong words', 'find this word', base_group]}
        expected = [{base_group: (base_group, 1.0)}]
        self.assertEqual(expected, strategy.apply_ngram(input_data))

        base_group = 'base group'
        untransformed_base_group = 'base | Group'
        input_data = {base_group: [untransformed_base_group, 'wrong | group']}
        expected = [{base_group: (untransformed_base_group, 1.0)}]
        self.assertEqual(expected, strategy.apply_ngram(input_data))
