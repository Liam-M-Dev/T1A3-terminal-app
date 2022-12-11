import json
import os

def directory_path():
    save_path = "./saved_files"
    if os.path.isdir(save_path) == False:
        os.mkdir(save_path)
    return save_path

def create_file(path, haiku):
    # Generate user input for file name
    translation_table = dict.fromkeys(map(ord, "!@#$ "), None)
    # While loop to prevent user from entering an empty string
    while True:
        file_name = input("Enter a name for your file: ")
        if file_name == "":
            print("file name cannot be an empty string!")
        else:
            break

    file_name = file_name.translate(translation_table) + ".json"
    full_path = path + "/" + file_name
    print(full_path)
    with open(full_path, "w") as file:
          json.dump(haiku, file, indent=4)


def list_of_files(directory):
    """Prints list of files in directory
        and checks user response is a valid file path"""
    print(os.listdir("./saved_files"))
    while True:
        user_selection = input("Enter the name of a file you want: ")
        user_selection = directory + "/" + user_selection
        if os.path.isfile(user_selection):
            return user_selection
        else:
            print("Sorry incorrect path, please type out file name:")
            
def load_appends(file_name, haiku):
    
    data = json.load(open(file_name))
    if type(data) is dict:
        data = [data]
    data.append(haiku)
    with open(file_name, "w") as file:
        json.dump(data, file, indent=4)


