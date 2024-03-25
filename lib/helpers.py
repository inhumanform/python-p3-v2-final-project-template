import sqlite3
# Utility and helper functions, mostly for your sql db

def connect_to_database(wine_database):
    conn = sqlite3.connect(wine_database)
    cursor = conn.cursor()
    return conn, cursor

def search_database(cursor, search_term):
    cursor.execute("SELECT * FROM parent_regions WHERE name LIKE ?", ('%' + search_term + '%',))
    parent_regions_results = cursor.fetchall()
    
    cursor.execute("SELECT * FROM subregions WHERE name LIKE ?", ('%' + search_term + '%',))
    subregions_results = cursor.fetchall()
    
    return parent_regions_results, subregions_results

def get_entry_details(cursor, table_name, entry_id):
    cursor.execute(f"SELECT * FROM {table_name} WHERE id=?", (entry_id,))
    entry_details = cursor.fetchone()
    return entry_details

def exit_program():
    print("Goodbye!")
    exit()
