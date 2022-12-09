import json

def create_file(title, haiku):
    with open(title, 'w') as file:
        json.dump(haiku, file, indent=4)