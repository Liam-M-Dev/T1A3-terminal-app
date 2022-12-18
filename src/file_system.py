try:
    import json
    import os
    import menu
    from pprint import pprint
except ImportError:
    print("There's been an error with imports, " \
    "please check modules are installed")
# Checks for saved files directory
# If directory doesn't exist, function creates the directory
def directory_path():
    save_path = "./saved_files"
    if not os.path.isdir(save_path):
        os.mkdir(save_path)
    return save_path

# Function to create save file path and write haiku into file
def create_file(path, file_name, haiku):
    
    full_path = path + "/" + file_name
    print(full_path)
    
    with open(full_path, "w") as file:
        json.dump(haiku, file, indent=4)

def create_file_name():
    translation_table = dict.fromkeys(map(ord, "!@#$%^&*()+=?>< ") \
    , None)
    # While loop to prevent user from entering an empty string
    while True:
        file_name = input("Enter a name for your file: ")
        menu.check_back_statement(file_name)
        if file_name.strip() == "" :
            print("file name cannot be an empty string!")
        else:
            break

    file_name = file_name.translate(translation_table) + ".json"
    return file_name

# Function to print files to user
# Giving the user the option to choose file they wish to work on
def list_of_files(directory):
    """Prints list of files in directory
        and checks user response is a valid file path"""
    print(os.listdir(directory))
    while True:
        user_selection = input("Enter the name of a file you want: ")
        menu.check_back_statement(user_selection)
        user_selection = directory + "/" + user_selection
        if os.path.isfile(user_selection):
            return user_selection
        else:
            user_selection = "Sorry incorrect file name, " \
             "please try again!"
            print(user_selection)
            

# Loads file and converts to list to append new haiku to data
def load_appends(file_name, haiku):
    data = json.load(open(file_name))
    if type(data) is dict:
        data = [data]
    data.append(haiku)
    with open(file_name, "w") as file:
        json.dump(data, file, indent=4)

def remove_file(file_name):
    try:
        os.remove(file_name)
    except FileNotFoundError:
        print("Sorry this file doesn't exist")

# Takes selected file from user and returns list of poems in file
def open_read_file(file_name):
    try:
        with open(file_name, "r") as file:
            poems = json.load(file)
            return poems
    except FileNotFoundError:
        print("Something has gone wrong with the file, " \
        "please try again")

def title_preview(poem_list):
    if type(poem_list) != list:
        poem_list = [poem_list]

    while True:
        i = 0
        while i < len(poem_list):
            print(poem_list[i]["title"])
            i += 1
        title_choice = input("Enter the title of the " \
            "poem you wish to edit: ")
        menu.check_back_statement(title_choice)

        for poem in poem_list:
            if title_choice.lower() == poem["title"].lower():
                print(f"you selected {poem['title']}")
                return poem
            else:
                pass
        input("Sorry the title was incorrect,"  \
            " press enter to try again")
        os.system("clear")
        

def poem_update(poem_list, updated_poem):
    if type(poem_list) is dict:
        poem_list = [poem_list]
    try:    
        for poem in poem_list:
            if poem["title"] == updated_poem["title"]:
                poem.update(updated_poem)
                break
            else:
                pass
        return poem_list
    except KeyError:
        print("Something has gone wrong with the poem, " \
            "please try again")

def file_update(file_name, updated_poem_list):
    try:
        with open(file_name, "w") as file:
            json.dump(updated_poem_list, file, indent=4)
    except FileNotFoundError:
        print("Something went wrong with the file name, " \
            "please try again:")

# opens file and prints out dictionaries to terminal
def view_file(file_name):
    try:
        with open(file_name, 'r') as file:
            data = json.load(file)
            pprint(data, sort_dicts=False)
    except FileNotFoundError:
        print("Sorry file does not exist")

def file_size(poem_file):
    if type(poem_file) != list:
        poem_file = [poem_file]

    if len(poem_file) >= 2:
        return poem_file
    else:
        return "Sorry this file does not " \
            "have enough poems to jumble"

