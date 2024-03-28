import sqlite3

from models.grape import Grape
from models.parentregion import ParentRegion
from models.subregion import SubRegion

# Utility and helper functions, mostly for your sql db

def connect_to_database(wine_database):
    conn = sqlite3.connect(wine_database)
    cursor = conn.cursor()
    return conn, cursor

def initialize_database():
    Grapes.get_all_grapes()
    Grapes.find_by_name()
    Grapes.find_by_id()
    Grapes.find_by_region()

    ParentRegion.get_all()
    SubRegion.get_all()

def search_database():
    while True:
        database_options_menu()
        user_input = input("How would you like your data:\n ")
        if(user_input == '1'):
            view_by_grapes()
            break
        elif (user_input == '2'):
            view_all_regions()
            break
        elif (user_input == '3'):
            display_menu()
            break


def database_options_menu():
    print("1. View Grape Varietals")
    print("2. View Wine Regions")
    print("3. Go back to the Main Menu")

def view_by_grapes_menu():
    print("1. Search by Grape Name")
    print("2. Search by Region")
    print("3. Search by ID")
    print("4. Show them all!")
    print("5. Back to Retrieve Wine Info")
    print("6. Back to Main Menu")
    
def view_by_grapes():
    while True:
        view_by_grapes_menu()
        user_input = input("\n How do you wanna search?:")
        # if(user_input == '1'):
        #     find_by_name(Grapes,name)
        #     break
        # elif(user_input == '2'):
        #     find_by_region()
        # elif(user_input == '3'):
        #     find_by_id()
        if(user_input == '4'):
           for grape in Grape.all:
            print(grape.name)
            break

   
        # if (user_input == '4'):
        #     for grape in Grapes.all:
        #         print(grape)
        #     break
        # elif (user_input == '2'):
        #     while True:
        #         try:
        #             user_input = ("\n Search grape by name...")
        #             user_input = str(user_input)
        #             grape = Grapes.find_by_name(user_input)
        #             if(grape):
        #                 print(Grapes.find_by_name(user_input))
        #             else:
        #                 print("That's not a real thing.")
        #                 user_input = input("\n Press any button to go back to the search menu.")
        #                 break
        #         except:
        #             print("Invalid input, I don't even know what that was.")
        #     break



def view_all_regions():
    print("1. Search by ID")
    print("2. Search by Name")
    print("3. Search by Climate")
    print("4. Search by Country")
    print("5. Search by Grapes grown")
    print("6. Back to Retrieve Wine Info")
    print("7. Back to Main Menu")

# def get_entry_details(cursor, table_name, entry_id):
#     cursor.execute(f"SELECT * FROM {table_name} WHERE id=?", (entry_id,))
#     entry_details = cursor.fetchone()
#     return entry_details



# def create_wines_table(cursor):
#     cursor.execute('''CREATE TABLE IF NOT EXISTS wines (
#                         id INTEGER PRIMARY KEY,
#                         name TEXT NOT NULL,
#                         region TEXT NOT NULL
#                     )''')

# def add_to_database(conn, cursor):
#     print("Adding to the database...")
    
    # Create the wines table if it doesn't exist
    # create_wines_table(cursor)

    # Collect data from the user
    # name = input("Enter wine name: ")
    # region = input("Enter region: ")

    # Insert data into the wines table
    # cursor.execute("INSERT INTO wines (name, region) VALUES (?, ?)", (name, region))
    # conn.commit()

    # print("Data added successfully.")

# if __name__ == "__main__":
#     conn = sqlite3.connect("wine_database.db")
#     cursor = conn.cursor()
    
#     add_to_database(conn, cursor)
    
#     conn.close()