#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sqlite3 as sqlite

con = sqlite.connect('db/uklotto.db')

with con:
    cur = con.cursor()
    cur.execute('SELECT N1, N2, N3, N4, N5, N6 FROM lotto where rowid<100')

    data = cur.fetchone()[0]

    print(f"SQLite version: {data}")
