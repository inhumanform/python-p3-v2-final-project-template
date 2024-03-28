import sqlite3


# Connects to the SQLite db file
CONN = sqlite3.connect('wine_database.db')

# Creates a cursor object
CURSOR = CONN.cursor()
