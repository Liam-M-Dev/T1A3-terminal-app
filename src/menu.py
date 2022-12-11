from haiku_poem import haiku_creator
from file_system import create_file
from file_system import directory_path

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

def saved_files():
    print("1: View saved poems from a file")
    print("2: Edit poems from a chosen file")
    print("3: Remove a file *Caution this will delete the file*")


def confirmation():
    confirm = input(" y or n: ")
    return confirm


# Haiku menu options
def new_haiku():
    haiku_loop = True
    save_path = directory_path()
    while haiku_loop == True:
        generate_poem = haiku_creator()
        print("Would you like to save poem?")
        save_to_new = confirmation()
        if save_to_new == "y":
            create_file(save_path, generate_poem)
            haiku_loop = False
        elif save_to_new == "n":
            break
        else:
            print("incorrect input please type y or n: ")

