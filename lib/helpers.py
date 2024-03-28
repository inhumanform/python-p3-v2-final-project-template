# import sqlite3

from models.grape import Grape
from models.parentregion import ParentRegion
from models.subregion import SubRegion

# Utility and helper functions, mostly for your sql db

# def connect_to_database(wine_database):
#     conn = sqlite3.connect(wine_database)
#     cursor = conn.cursor()
#     return conn, cursor

def initialize_database():
    Grape.get_all_grapes()
    Grape.create_table()
    ParentRegion.get_all()
    ParentRegion.create_table()
    SubRegion.get_all_subregions()
    SubRegion.create_table()

def search_database():
    while True:
        database_options_menu()
        user_input = input("Choose:\n ")
        if(user_input == '1'):
            search_by_grapes()
            break
        elif (user_input == '2'):
            display_menu()
            break
        


def database_options_menu():
    print("1. Search")
    print("2. Go back to the Main Menu")
    

def search_by_grapes_menu():
    print("1. Search by Grape Name")
    print("2. Search by Region")
    print("3. Search by ID")
    print("4. Show them all!")
    print("5. Back to Retrieve Wine Info")
    print("6. Back to Main Menu")
    
def search_by_grapes():
    search_by_grapes_menu()
    user_input = input("\n How do you wanna search?:")

    while True:
        if(user_input == '1'):
           while True:
                try:
                    user_input = input("Enter the name of a grape varietal: ")
                    user_input = str(user_input)
                    artist = Grape.find_by_name(user_input)
                    if(grape):
                         print("\nMatching Results")
                         print(Grape.find_by_name(user_input))
                    else:
                         print("No varietals found")
                    user_input = input("\n Press 'return' to continue.")
                    break
                except:
                     print("Invalid input, please try again.")
                break
        elif(user_input == '2'):
           search_by_region_menu()
           user_input = input("Select Search Parameters: ")
           while True:
                try:
                    print("\nYour Region must match one in the database!")
                    user_input = input("Enter the name of a region: ")
                    user_input = str(user_input)
                    grape = Grape.find_by_region(user_input)
                    if(grape):
                         print("\nHere are the grapes from this region")
                         print(Grape.find_by_region(user_input))
                    else:
                         print("No region was found by that name")
                    user_input = input("\n Press 'return' to continue.")
                    break
                except:
                     print("Invalid input, please try again.")
                break

        elif(user_input == '3'):
           while True:
                try:
                    user_input = input("\nEnter the id number for the grape varietal ")
                    user_input = int(user_input)
                    grape = Grape.find_by_id(user_input)
                    if(grape):
                        print("\nGrape matching ID")
                        print(Grape.find_by_id(user_input))
                    else:
                            print("\nNo grapes exist with this id!")
                    user_input = input("\n Press 'return' to continue.")
                    break
                except:
                        print("Invalid input, please try again.")
                break
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



def search_by_region_menu():
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