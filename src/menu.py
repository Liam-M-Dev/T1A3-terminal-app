from haiku_poem import haiku_creator
from file_system import create_file

# Menu options for main menu
def main_menu():
    print("1: Intro")
    print("2: Create Haiku")
    print("3: Saved Files")
    print("4: Jumbler")
    print("5: Quit")
    
    while True:
        try:
            main_option = int(input("Select menu option (1-5): "))
            break      
        except ValueError:
            print("Incorrect input, please try again")


    return main_option


def create_old():
    print("1: Create new file")
    print("2: Open file to save into")

    while True:
        try:
            user_input = int(input("Select menu option (1-2): "))
            break      
        except ValueError:
            print("Incorrect input, please try again")
    
    return user_input


def confirmation():
    confirm = input(" y or n: ")
    return confirm.toLower()


# Haiku menu options
def new_haiku():
    haiku_loop = True
    while haiku_loop == True:
        generate_poem = haiku_creator()
        save_to_new = confirmation()
        if save_to_new == "y":
            create_file(generate_poem)
            make_another = "n"
            while make_another == "n":
                make_another = input("Would you like to make another, y or n: ")
                if make_another == "y":
                    break
                if make_another == "n":
                    haiku_loop = False
        elif save_to_new == "n":
            pass
        else:
            print("incorrect input please type y or n: ")