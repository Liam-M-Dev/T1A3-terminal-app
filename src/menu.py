try:
    from haiku_poem import haiku_creator
    from haiku_poem import poem_editor
    import json
    import file_system
    from jumbler import randomiser
except ImportError:
    print("There's been an error with imports, please check modules are installed")

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

    check_back_statement(confirm)

    return confirm


def menu_selection():
    while True:
        try:
            user_input = input("Select menu option: ")
            check_back_statement(user_input)
            user_input = int(user_input)
            break      
        except ValueError:
            print("Incorrect input, please try again")
    
    return user_input

def check_back_statement(back_statement):
    if back_statement == "back":
        raise KeyboardInterrupt

# Haiku menu options
def new_haiku():
    haiku_loop = True
    save_path = file_system.directory_path()
    
    while haiku_loop == True:
        generate_poem = haiku_creator()
        print("Would you like to save poem?")
        while True:
            save_to_new = confirmation()
            if save_to_new.lower() == "y":
                new_file = file_system.create_file_name()
                file_system.create_file(save_path, new_file, \
                     generate_poem)
                input("Poem saved, press enter to return: ")
                haiku_loop = False
                break
            elif save_to_new.lower() == "n":
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
            print("Incorrect input, please select 1 or 2: ")
            selection = menu_selection()
            

def saved_files_system(selection, directory):
    load = file_system.list_of_files(directory)
    if selection == 1: # prints out the poems on terminal
        file_system.view_file(load)
    elif selection == 2: # Allows user to edit poems within a file
        get_poem_list = file_system.open_read_file(load)
        get_title = file_system.title_preview(get_poem_list)
        update_poem = poem_editor(get_title)
        final_poem = file_system.poem_update(get_poem_list, update_poem)
        file_system.file_update(load, final_poem)
    elif selection == 3: # removes file from the directory
        print("are you sure? ")
        delete_file = confirmation()
        if delete_file == "y":
            file_system.remove_file(load)
        elif delete_file == "n":
            print("Ok going back to menu")
    else:
        print("Something has gone wrong sorry!")

def jumbler_system(directory):
    file_select = file_system.list_of_files(directory)
    get_poems = file_system.open_read_file(file_select)
    file_check = file_system.file_size(get_poems)
    if file_check != get_poems:
        return "not enough poems, please try again"
    else:
        while True:
            jumble_poem = randomiser(get_poems)
            print("Would you like to save this poem? ")
            choice = confirmation()
            if choice == "y":
                file_system.load_appends(file_select, jumble_poem)
                input(f"Saved to {file_select}, Press enter to jumble again")
            elif choice == "n":
                print("No worries, jumble again!")
            else: 
                print("Sorry I didn't recognize that, please try again")
        
        