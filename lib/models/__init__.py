import sqlite3

CONN = sqlite3.connect('wine_database.db')
CURSOR = CONN.cursor()
