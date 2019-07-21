import path_handler
import os
import random
import subprocess


def get_list_of_pics():
    dir_path = path_handler.get_path()  # TODO: this makes this module dependent on path_handler :/
    picture_names = os.listdir(dir_path)  # TODO: check extensions of files
    picture_paths = [os.path.join(dir_path, pic) for pic in picture_names]  # TODO: os.path.realpath?
    return picture_paths


def get_random_picture():
    list_of_pictures = get_list_of_pics()
    return random.choice(list_of_pictures)


def set_background():
    pic_path = get_random_picture()
    desktop_setter = ["gsettings", "set", "org.gnome.desktop.background", "picture-uri", "file://" + pic_path]
    subprocess.run(desktop_setter)
    lock_screen_setter = ["gsettings", "set", "org.gnome.desktop.screensaver", "picture-uri", "file://" + pic_path]
    subprocess.run(lock_screen_setter)
