from os import system
from menu import main_menu
from intro import intro_printout

# Variable to handle start and stopping for main menu loop
start_stop = True

# Loop for program start, access main menu function from menu.py
# User input converted to int to select from menu.
# Option 5 exits loop by changing start_stop to False
while start_stop == True:
    system("clear")

    menu_option = main_menu()
    system("clear")

    if menu_option == 1:
        print(intro_printout())
        input("Press Enter to return:")
    elif menu_option == 2:
        print("Create haiku page")
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
        

    