from random import shuffle
import json


# Take user input to open up a selected file to randomize
# check file selected has more than one poem
def file_size(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
        if len(data) >= 2:
            return data
        else:
            print("Unfortunately this file doesn't have enough poems")

# randomize the file with shuffle
def randomiser(poem_data):
    pass
# return the mess of a file to the viewer to see
# ask if they would like to save file or return to the menu

randomiser(file_size("./saved_files/sample_poems.json"))