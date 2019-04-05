#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sqlite3 as sqlite
import sys

con = None

try:
    con = sqlite.connect('db/uklotto.db')

    cur = con.cursor()
    cur.execute('SELECT SQLITE_VERSION()')

    data = cur.fetchone()[0]

    print(f"SQLite version: {data}")

except sqlite.Error as e:

    print(f"Error {e.args[0]}")
    sys.exit(1)

finally:

    if con:
        con.close()
