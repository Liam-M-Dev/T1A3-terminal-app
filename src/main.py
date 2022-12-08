from os import system
from menu import main_menu
from intro import intro_printout


menu_option = ""
# Main menu loop
while menu_option != "5":
    system("clear")
    menu_option = main_menu()
    system("clear")
    if menu_option == "1":
        print(intro_printout())
        input("Press Enter to return:")
    elif menu_option == "2":
        print("Create haiku page")
        input("Press Enter to return:")
    elif menu_option == "3":
        print("Saved files")
        input("Press Enter to return:")
    elif menu_option == "4":
        print("jumbler")
        input("Press Enter to return:")
    elif menu_option == "5":
        print("Exits program!")
        input("Press Enter to return:")
    else:
        print("Sorry not a valid input, please select from the options")
        input("Press Enter to return:")
        

    