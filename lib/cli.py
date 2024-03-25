# Here we are going to handle user input, display messages, and interact with the db. Welcome screen, menu options, logic for the menu options, etc.

from helpers import connect_to_database, search_database, get_entry_details

def welcome_screen():
    print("********************************************")
    print("Welcome to the Wine Database")
    print("********************************************")

def display_menu():
    print("\nSelect an option:")
    print("1. Retrieve Wine Info")
    print("2. Add to the Database")
    print("3. About this Program")
    print("4. Exit")

def search_wine(cursor):
    search_term = input("Enter your search term: ")
    parent_regions_results, subregions_results = search_database(cursor, search_term)
    print("Parent Regions:")
    for result in parent_regions_results:
        print(result)
    print("Subregions:")
    for result in subregions_results:
        print(result)

def add_to_database(conn, cursor):
    print("Adding to the database...")
    # Add logic to collect data from user and insert into database tables
    # For example:
    name = input("Enter wine name: ")
    region = input("Enter region: ")
    # Insert data into database
    cursor.execute("INSERT INTO wines (name, region) VALUES (?, ?)", (name, region))
    conn.commit()
    print("Data added successfully.")

    
def main():
    conn, cursor = connect_to_database("wine_database.db")
    
    while True:
        welcome_screen()
        display_menu()
        choice = input("Enter your choice: ")
        
        if choice == '1':
            search_wine(cursor)
        elif choice == '2':
            add_to_database(conn, cursor)
        elif choice == '3':
            about_program()
        elif choice == '4':
            print("Exiting...")
            break  # Exit the loop and end the program
        else:
            print("Invalid choice. Please try again.")
        
    conn.close()

if __name__ == "__main__":
    main()
