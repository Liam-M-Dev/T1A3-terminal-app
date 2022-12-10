import syllapy
# from pprint import pprint

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
    
    print(f"{poem_title} {poem['line_one']} {poem['line_two']} {poem['line_three']}")
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
        if line_count < 5 or line_count > 5:
            print("Incorrect amount of syllables, try again")
        else:
            return user_input

# Function to get user input for line 2
# checks syllable count and returns user input
def seven_syllable_line():
    while True:
        user_input = input("Enter line: ")
        line_count = syllable_counter(user_input)
        if line_count < 7 or line_count > 7:
            print("Incorrect amount of syllables, try again")
        else:
            return user_input


