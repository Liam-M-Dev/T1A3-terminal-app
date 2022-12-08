from os import system
from menu import main_menu


menu_option = ""
# Main menu loop
while menu_option != "5":
    system("clear")
    menu_option = main_menu()
    if menu_option == "1":
        print("This is the intro page")
    elif menu_option == "2":
        print("Create haiku page")
    elif menu_option == "3":
        print("Saved files")
    elif menu_option == "4":
        print("jumbler")
    else:
        print("Exits program!")
    