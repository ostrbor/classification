from models import Products1, Products2
from group_relations import GroupRelations, GroupRelation


class DatabaseApi:
    @classmethod
    def get_distinct_groups_combination(cls) -> GroupRelations:
        qry = (Products1.select(Products1.category,
                                Products2.eshop_category).distinct()
               .join(Products2, on=(Products1.plu == Products2.plu)).tuples())
        res = [GroupRelation(record[0], record[1]) for record in qry]
        return GroupRelations(res)
