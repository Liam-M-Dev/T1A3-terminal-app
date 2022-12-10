import json
import os

def create_file():
    # Initiate path to save file to
    save_path = "./saved_files/"
    # Generate user input for file name
    translation_table = dict.fromkeys(map(ord, "!@#$ "), None)
    file_name = input("Enter a name for your file: ")
    file_name = file_name.translate(translation_table) + ".json"
    print(file_name)
    full_path = save_path + file_name
    print(full_path)
    # with open(save_path, 'w') as file:
    #      json.dump(haiku, file, indent=4)

create_file()