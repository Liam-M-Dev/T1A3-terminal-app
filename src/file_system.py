import json
import os

def create_file(haiku):
    # Initiate path to save file to
    save_path = "./saved_files/"
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
    full_path = save_path + file_name
    print(full_path)
    with open(full_path, 'w') as file:
          json.dump(haiku, file, indent=4)

