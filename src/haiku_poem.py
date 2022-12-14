import syllapy
import terminal
import menu
from os import system


def haiku_creator():
    poem = {}
    
    # Get user input to create title of poem
    poem_title = input("Enter a title for your poem: ")
    menu.check_back_statement(poem_title)
    poem["title"] = poem_title
    
    # Gets user input and checks syllable count
    # appends value to poem line keys
    poem["line_one"] = five_syllable_line()
    poem["line_two"] = seven_syllable_line()
    poem["line_three"] = five_syllable_line()
    system("clear")
    print(f"Title: {terminal.bold(poem_title)}\n"  
            + f"{terminal.italic(poem['line_one'])}\n" 
            + f"{terminal.italic(poem['line_two'])}\n" 
            + f"{terminal.italic(poem['line_three'])}")
    return poem

# Function called to use syllapy module to count syllables
def syllable_counter(line):
    count = syllapy.count(line)
    return count


# Function to get user input for line 1 and 3
# checks syllable count and returns user input
def five_syllable_line():
    while True:
        user_input = input("Enter line: ")
        menu.check_back_statement(user_input)
        line_count = syllable_counter(user_input)
        print(line_count)
        if line_count < 4:
            user_input = f"Not enough syllables, syllable count {line_count}"
            print(user_input)
        elif line_count > 6:
            user_input = f"Too many syllables, syllable count {line_count}"
            print(user_input)
        else:
            return user_input

# Function to get user input for line 2
# checks syllable count and returns user input
def seven_syllable_line():
    while True:
        user_input = input("Enter line: ")
        menu.check_back_statement(user_input)
        line_count = syllable_counter(user_input)
        if line_count < 6:
            user_input = f"Not enough syllables, syllable count {line_count}"
            print(user_input)
        elif line_count > 8:
            user_input = f"Too many syllables, syllable count {line_count}"
            print(user_input)
        else:
            return user_input


def poem_editor(poem):
    try:
        while True:
            line_input = line_selection()
            if line_input == "line_one":
                poem["line_one"] = five_syllable_line()
            elif line_input == "line_two":
                poem["line_two"] = seven_syllable_line()
            elif line_input == "line_three":
                poem["line_three"] = five_syllable_line()
            else:
                line_input = """Please select the line you want by typing
                line_one, line_two or line_three"""
                print(line_input)
    except ValueError:
        input("Press enter to save:")
        return poem
            


def line_selection():
    print("""Enter the line you want to edit by typing
    line_one, line_two or line_three, type back when finished""")
    choice = input("")

    if choice == "done":
        raise ValueError

    return choice

