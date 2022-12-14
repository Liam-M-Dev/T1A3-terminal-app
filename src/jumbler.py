try:
    from random import shuffle
except ImportError:
    print("There's been an error with imports," 
    "please check modules are installed")


# Take user input to open up a selected file to randomize
# check file selected has more than one poem


# randomize the file with shuffle
def randomiser(poem_data):
    list_values = []
    dictionary_keys = []
    for poem in poem_data:
        list_values += poem.values()
        dictionary_keys += poem.keys()
    shuffle(list_values)
    shuffled = dict(zip(dictionary_keys, list_values))
    print(shuffled)
    return shuffled

