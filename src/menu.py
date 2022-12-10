

# Menu options for main menu
def main_menu():
    print("1: Intro")
    print("2: Create Haiku")
    print("3: Saved Files")
    print("4: Jumbler")
    print("5: Quit")
    
    while True:
        try:
            main_option = int(input("Select menu option (1-5): "))
            break      
        except ValueError:
            print("Incorrect input, please try again")


    return main_option


def create_old():
    print("1: Create new file")
    print("2: Open file to save into")