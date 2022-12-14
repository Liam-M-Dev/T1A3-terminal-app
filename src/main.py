from os import system
import menu
import file_system
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
    try:
        menu.main_menu()
        menu_option = menu.menu_selection()
        system("clear")

        if menu_option == 1:
            intro_printout()
            input("Press Enter to return:")
        elif menu_option == 2:
            menu.create_old()
            menu.create_haiku_system(menu.menu_selection(), save_path)
            
        elif menu_option == 3:
            menu.saved_files()
            menu.saved_files_system(menu.menu_selection(), save_path)
            input("Press Enter to return:")
        elif menu_option == 4:
            print(menu.jumbler_system(save_path))
            input("Press Enter to return:")
        elif menu_option == 5:
            print("Exits program!")
            start_stop = False
        else:
            print("Sorry not a valid input, please select from the options")
            input("Press Enter to return:")
    except KeyboardInterrupt:
        input("Back to main menu: ")        

    