#! /usr/bin/env python
from db_api import DatabaseApi
from strategies import Bijection, Ngram
from create_result_db import create_tables


def print_stategy_result(strategy):
    name = strategy.__class__.__name__
    input_data_count = len(strategy.grouped_categories)
    result_count = len(strategy.result_categories)
    print(f'{name} approach extracted {result_count} from {input_data_count}')
    print(f'Efficiency of {name} is {strategy.calculate_efficiency()}%\n')


if __name__ == '__main__':
    create_tables()
    data = DatabaseApi.get_distinct_groups_combination()
    print(f'There are {len(data)} distinct group combinations with one-to-many relations to process with Bijection.')

    set_strategy = Bijection(data)
    bijective_groups = set_strategy.process()
    bijective_groups.save_bijection_results()
    print_stategy_result(set_strategy)

    groups_to_apply_ngrams = data - bijective_groups
    print(
        f'There are {len(groups_to_apply_ngrams)} distinct group combinations with one-to-many relations to process with Ngram.')

    ngram_strategy = Ngram(groups_to_apply_ngrams)
    ngram_groups = ngram_strategy.process()
    ngram_groups.save_ngram_results()
    print_stategy_result(ngram_strategy)
