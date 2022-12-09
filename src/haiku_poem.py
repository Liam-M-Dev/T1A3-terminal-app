import syllapy

def haiku_creator():
    poem = {}
    # Get user input to create title of poem
    poem_title = input("Enter a title for your poem: ")
    poem["title"] = poem_title
    # Get user input for each line of poem
    
    poem["line_one"] = five_syllable_line()
    poem["line_two"] = seven_syllable_line()
    poem["line_three"] = five_syllable_line()
    # Check each line for syllable requirements
    # Append lines to empty dictionary
    # return dictionary
    print(poem)
    return poem

def syllable_counter(line):
    count = syllapy.count(line)
    return count

def five_syllable_line():
    while True:
        user_input = input("Enter line: ")
        line_count = syllable_counter(user_input)
        if line_count < 5 or line_count > 5:
            print("Incorrect amount of syllables, try again")
        else:
            return user_input

def seven_syllable_line():
    while True:
        user_input = input("Enter line: ")
        line_count = syllable_counter(user_input)
        if line_count < 7 or line_count > 7:
            print("Incorrect amount of syllables, try again")
        else:
            return user_input


haiku_creator()