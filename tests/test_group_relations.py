from unittest import TestCase
from group_relations import GroupRelations, GroupRelation


class GroupsTest(TestCase):
    def setUp(self):
        self.data = [('a', 'A'), ('b', 'B')]

    def test_convert(self):
        expected = [GroupRelation('a', 'A'), GroupRelation('b', 'B')]
        self.assertEqual(expected, GroupRelations(self.data).data)

    def test_sub(self):
        data_minor = [('a', 'A')]
        group_rels_major = GroupRelations(self.data)
        group_rels_minor = GroupRelations(data_minor)
        expected = GroupRelations([('b', 'B')])
        res = group_rels_major - group_rels_minor
        self.assertEqual(expected.data, res.data)

    def test_iteration(self):
        data = GroupRelations(self.data)
        res = []
        for i in data:
            res.append(i[0])
        expected = ['a', 'b']
        self.assertEqual(expected, res)