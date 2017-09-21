from db_api import DatabaseApi
from models import create_tables
from strategies import SetStrategy


class NgramsStrategy:
    pass


if __name__ == '__main__':
    create_tables()
    api = DatabaseApi()
    data = api.get_distinct_categories_combination()
    set_strategy = SetStrategy(data)
    set_strategy.process()
