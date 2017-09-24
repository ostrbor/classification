from group_relations import GroupRelations


class Strategy:
    grouped_categories = None  # operate upon it
    result_categories = None  # result with one-to-one relations

    def __init__(self, group_relations: GroupRelations):
        self.group_relations = group_relations  # input with one-to-many relations

    def process(self) -> GroupRelations:
        raise NotImplemented

    def calculate_efficiency(self):
        return int(len(self.result_categories) / len(self.grouped_categories) * 100)
