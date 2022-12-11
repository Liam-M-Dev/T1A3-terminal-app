import syllapy
import terminal
from os import system

def haiku_creator():
    poem = {}
    
    # Get user input to create title of poem
    poem_title = input("Enter a title for your poem: ")
    poem["title"] = poem_title
    
    # Gets user input and checks syllable count
    # appends value to poem line keys
    poem["line_one"] = five_syllable_line()
    poem["line_two"] = seven_syllable_line()
    poem["line_three"] = five_syllable_line()
    system("clear")
    print(f"Title: {poem_title}\n"  
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
        line_count = syllable_counter(user_input)
        print(line_count)
        if line_count < 5:
            user_input = f"Not enough syllables, syllable count {line_count}"
            print(user_input)
        elif line_count > 5:
            user_input = f"Too many syllables, syllable count {line_count}"
            print(user_input)
        else:
            return user_input

# Function to get user input for line 2
# checks syllable count and returns user input
def seven_syllable_line():
    while True:
        user_input = input("Enter line: ")
        line_count = syllable_counter(user_input)
        if line_count < 7:
            user_input = f"Not enough syllables, syllable count {line_count}"
            print(user_input)
        elif line_count > 7:
            user_input = f"Too many syllables, syllable count {line_count}"
            print(user_input)
        else:
            return user_input
