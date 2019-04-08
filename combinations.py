#!/usr/bin/python

import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return None


def create_combinations(iterable, r):
    """
    Create all unique sets of r length from the iterable input
    :param iterable: a list or tuple containing a number of variables
    :param r: the length of the subset to find in the variable e.g. all sets of 3 numbers from 6 given
    :return: A list holding all unique sets
    """
    j = iterable
    unique_set = []
    print(j)
    for comb in j:
        unique_set.insert(comb)
    return unique_set


def select_draws(conn, x):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM lotto WHERE DrawID <= " + str(x))
    num = []
    rows = cur.fetchall()
    for row in rows:
        # print(row)
        # num.append(row[0])
        num.append(row[5:11])
        print(num)
    return num


def main():
    database = "/home/lol/PycharmProjects/lottery/db/uklotto.db"

    # create a database connection
    conn = create_connection(database)
    with conn:
        print("Get the first 100 draws")
        draws = select_draws(conn, 10)
        result = []
        for draw in draws:
            print(draw)
            combo = create_combinations(draw, 3)
            print(combo)
            result.append(draw)
            result.append(combo)
        print(result)


if __name__ == '__main__':
    main()
