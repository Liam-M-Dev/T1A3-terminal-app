from random import shuffle
from file_system import file_size
from file_system import open_read_file


# Take user input to open up a selected file to randomize
# check file selected has more than one poem


# randomize the file with shuffle
def randomiser(poem_data):
    list_values = []
    dictionary_keys = []
    for poem in poem_data:
        list_values += poem.values()
        dictionary_keys += poem.keys()
    print(list_values)
    shuffle(list_values)
    print(dictionary_keys)
    shuffled = dict(zip(dictionary_keys, list_values))
    print(shuffled)
    return shuffled

# return the mess of a file to the viewer to see
# ask if they would like to save file or return to the menu

# randomiser(file_size(open_read_file("./saved_files/sample_poems.json")))