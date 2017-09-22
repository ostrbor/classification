from unittest import TestCase
from groups import Groups, Group


class GroupsTest(TestCase):
    def test_convert(self):
        data = [(1, 2), (3, 4)]
        expected = [Group(1, 2), Group(3, 4)]
        self.assertEqual(expected, Groups(data).data)
