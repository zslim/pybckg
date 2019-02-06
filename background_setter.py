import path_handler
import os
import random
import subprocess


def get_list_of_pics():
    dir_path = path_handler.get_path()
    picture_names = os.listdir(dir_path)
    picture_paths = [os.path.join(dir_path, pic) for pic in picture_names]
    return picture_paths


def get_random_picture():
    list_of_pictures = get_list_of_pics()
    return random.choice(list_of_pictures)


def set_background():
    pic_path = get_random_picture()
    shell_command = ["gsettings", "set", "org.gnome.desktop.background", "picture-uri", "file://" + pic_path]
    subprocess.run(shell_command)
