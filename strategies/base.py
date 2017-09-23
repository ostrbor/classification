from group_relations import GroupRelations


class Strategy:
    def __init__(self, group_relations: GroupRelations):
        self.group_relations = group_relations

    def process(self) -> GroupRelations:
        raise NotImplemented