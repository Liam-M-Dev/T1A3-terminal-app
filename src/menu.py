from haiku_poem import haiku_creator
from haiku_poem import poem_editor
import json
import file_system

# Menu options for main menu
def main_menu():
    print("1: Intro")
    print("2: Create Haiku")
    print("3: Saved Files")
    print("4: Jumbler")
    print("5: Quit")


def create_old():
    print("1: Create new file")
    print("2: Open file to save into")


def saved_files():
    print("1: View saved poems file")
    print("2: Edit poems from a chosen file")
    print("3: Remove a file *Caution this will delete the file*")

    


def confirmation():
    confirm = input(" y or n: ")
    return confirm


def menu_selection():
    while True:
        try:
            user_input = int(input("Select menu option: "))
            break      
        except ValueError:
            print("Incorrect input, please try again")
    
    return user_input


# Haiku menu options
def new_haiku():
    haiku_loop = True
    save_path = file_system.directory_path()
    while haiku_loop == True:
        generate_poem = haiku_creator()
        print("Would you like to save poem?")
        save_to_new = confirmation()
        if save_to_new == "y":
            file_system.create_file(save_path, generate_poem)
            haiku_loop = False
        elif save_to_new == "n":
            break
        else:
            print("incorrect input please type y or n: ")

def create_haiku_system(selection, directory):
    while True:
        if selection == 1:
            new_haiku()
            break
        elif selection == 2:
            file_path = file_system.list_of_files(directory)
            poem = haiku_creator()
            try:
                file_system.load_appends(file_path, poem)
                break
            except json.decoder.JSONDecodeError:
                print("Oh no there's no poems in this file to add to")
                input("Press enter to return to the menu") 
        else:
            print("please choose 1 or 2:")
            input("Press Enter to return:")

def saved_files_system(selection, directory):
    load = file_system.list_of_files(directory)
    if selection == 1:
        file_system.view_file(load)
    elif selection == 2:
        get_poem_list = file_system.open_read_file(load)
        get_title = file_system.title_preview(get_poem_list)
        get_poem = file_system.poem_return(get_poem_list, get_title)
        update_poem = poem_editor(get_poem)
        final_poem = file_system.poem_update(get_poem_list, update_poem)
        file_system.file_update(load, final_poem)
    elif selection == 3:
        print("are you sure? ")
        delete_file = confirmation()
        if delete_file == "y":
            file_system.remove_file(load)
        elif delete_file == "n":
            print("Ok going back to menu")
    else:
        print("Something has gone wrong sorry!")
