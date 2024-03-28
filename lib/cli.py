# Here we are going to handle user input, display messages, and interact with the db. Welcome screen, menu options, logic for the menu options, etc.
from models.__init__ import CONN, CURSOR
import ipdb
from helpers import (
    initialize_database, 
    search_database)
from models.grape import Grape

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
    print("1. Retrieve Wine Info")
    print("2. Add to the Database")
    print("3. About this Program")
    print("4. Exit")
   

def about_program():
    print("WineCLI is a simple tool for wine enthusiasts to retrieve, view, and update information about the wine world. \n\nThis interface was built by Drew Hairston for a project while at Flatiron School.  ")

def add_to_database():
    name = input('Enter the name of your grape varietal:')
    color = input('What color is your grape?:')
    key_growing_regions = input('Where is your grape from?')
    parentage = input('Does your grape have parent grapes?:')
    ipdb.set_trace()
    new_grape = Grape.create(name, color, key_growing_regions, parentage)
    new_grape.save()
    print("Adding to the database...")

    print("Data added successfully.")


def exit_program():
    print("Later, nerd...")
    exit()

if __name__ == "__main__":
    main()
