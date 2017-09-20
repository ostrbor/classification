from collections import namedtuple
from .models import Products1, Products2


class DatabaseApi:
    def __init__(self):
        self.categories = namedtuple('Categories', ['base', 'derivative'])

    def get_distinct_categories_combination(self):
        qry = (Products1.select(Products1.category,
                                Products2.eshop_category).distinct()
               .join(Products2, on=(Products1.plu == Products2.plu)).tuples())
        return [self.categories(record[0], record[1]) for record in qry]
