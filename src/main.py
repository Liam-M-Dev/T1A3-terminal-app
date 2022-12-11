from os import system
import json
import menu
import file_system
import haiku_poem
from intro import intro_printout


# Variable to handle start and stopping for main menu loop
start_stop = True

# Sets global variable for saved_files path
save_path = file_system.directory_path()

# Loop for program start, access main menu function from menu.py
# User input converted to int to select from menu.
# Option 5 exits loop by changing start_stop to False
while start_stop == True:
    system("clear")

    menu_option = menu.main_menu()
    system("clear")

    if menu_option == 1:
        intro_printout()
        input("Press Enter to return:")
    elif menu_option == 2:
        user_input = menu.create_old()
        if user_input == 1:
            menu.new_haiku()
        elif user_input == 2:
            file_path = file_system.list_of_files(save_path)
            poem = haiku_poem.haiku_creator()
            try:
                file_system.load_appends(file_path, poem)
            except json.decoder.JSONDecodeError:
                print("Oh no there's no poems in this file to add to")
                input("Press enter to return to the menu") 
        else:
            print("please choose 1 or 2:")
            input("Press Enter to return:")
    elif menu_option == 3:
        print("Saved files")
        input("Press Enter to return:")
    elif menu_option == 4:
        print("jumbler")
        input("Press Enter to return:")
    elif menu_option == 5:
        print("Exits program!")
        start_stop = False
    else:
        print("Sorry not a valid input, please select from the options")
        input("Press Enter to return:")
        

    