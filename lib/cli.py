# Here we are going to handle user input, display messages, and interact with the db. Welcome screen, menu options, logic for the menu options, etc.
from models.__init__ import CONN, CURSOR
from helpers import (
    initialize_database, 
    search_database

)

def main():
    initialize_database()

    while True:
        welcome_screen()
        display_menu()
        user_input = input ("\n\nWhere do you wanna go?\n")
        
        if (user_input == '1'):  
            search_database()  
            break
        elif (user_input == '2'):
            add_to_database()
            break
        elif (user_input == '3'):
            about_program()
            break
        elif (user_input == '4'):
            exit_program()
            break
        else:
            print("Pick an actual option, dumbass")
        

def welcome_screen():
    print("********************************************")
    print("Welcome to the Wine Database")
    print("\n********************************************")

def display_menu():
    menu_options = (
        "1. Retrieve Wine Info",
        "2. Add to the Database",
        "3. About this Program",
        "4. Exit"
    )
    print(menu_options)

def exit_program():
    print("Later, nerd...")
    exit()

if __name__ == "__main__":
    main()
