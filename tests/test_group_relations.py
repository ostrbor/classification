from unittest import TestCase
from group_relations import GroupRelations, GroupRelation


class GroupsTest(TestCase):
    def test_convert(self):
        data = [(1, 2), (3, 4)]
        expected = [GroupRelation(1, 2), GroupRelation(3, 4)]
        self.assertEqual(expected, GroupRelations(data).data)
