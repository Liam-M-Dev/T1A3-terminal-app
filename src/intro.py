try:
    import terminal
except ImportError:
    print("Something went wrong with the file name, " \
        "please try again:")
# Introduction to haiku creator

# Function to print out introduction and basic rules

def intro_printout():
    intro_text = """
    Hello and welcome to haiku creator
    This terminal app allows you to create your own haiku poems.
    
    So what is a haiku you ask?
    A haiku is a small poem consisting of 3 lines and 17 syllables,
    depicting a moment of insight followed by a moment of observation.

    You can create your haiku in the create a haiku option.
    The logic will then determine if it follows the basic rule of:
    5 syllables in the first and third line, 7 syllables in the second.
    Well almost, I have given you a little le-way since modern
    haiku's don't exactly follow the 5-7-5 rule.
    So you can enter 4 to 6 for lines one and three
    and 6 to 8 for line 2.

    You can also view and edit your files in the saved file option.
    For extra fun, try the jumble option to jumble your haiku's in
    the selected file!

    **type back at any prompt to get back to the main menu!
    """

    print(terminal.green(intro_text)) 

