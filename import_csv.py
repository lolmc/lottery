# Import `os`
import os

# Import module to deal with IP subnet calculations

# Retrieve current working directory (`cwd`)
cwd = os.getcwd()
print(cwd)
# Change directory
os.chdir("/home/lol/PycharmProjects/lottery/")
# List all files and directories in current directory
print(os.listdir('.'))

# Adventure with sqlite3

# A minimal SQLite shell for experiments

import sqlite3

con = sqlite3.connect(":memory:")
con.isolation_level = None
cur = con.cursor()

buffer = ""

print("Enter your SQL commands to execute in sqlite3.")
print("Enter a blank line to exit.")

while True:
    line = input()
    if line == "":
        break
    buffer += line
    if sqlite3.complete_statement(buffer):
        try:
            buffer = buffer.strip()
            cur.execute(buffer)

            if buffer.lstrip().upper().startswith("SELECT"):
                print(cur.fetchall())
        except sqlite3.Error as e:
            print("An error occurred:", e.args[0])
        buffer = ""

con.close()
