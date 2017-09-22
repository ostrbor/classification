#! /usr/bin/env python
from db_api import DatabaseApi
from strategies import Bijection

if __name__ == '__main__':
    data = DatabaseApi.get_distinct_groups_combination()
    set_strategy = Bijection(data)
    bijective_groups = set_strategy.process()
    print(f'From {len(data)} distinct groups combination extracted {len(bijective_groups)} bijective groups.')
    groups_to_apply_ngrams = data - bijective_groups
    print(f'There are {len(groups_to_apply_ngrams)} groups for Ngram algorithm.')
