#! /usr/bin/env python
from models import result_database, Prediction


def create_tables():
    """
    To create database, if it doesn't exist.
    """
    result_database.connect()
    result_database.create_tables([Prediction])


if __name__ == '__main__':
    create_tables()
