import os

PATH_FILE = "path_to_dir.txt"


def get_path():
    with open(PATH_FILE, "r+") as f:
        dir_path = f.read()
        if not os.path.isdir(dir_path):
            dir_path = get_path_input("Please enter the absolute path to the folder that contains your pictures: ")
            f.write(dir_path)
    return dir_path


def get_path_input(message):
    user_input = input(message)

    while not os.path.isdir(user_input):  # TODO: could crash if automatized
        print("Invalid path: ", user_input)
        user_input = input(message)

    return user_input
