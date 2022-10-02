"""Translated Blaze config to Kitty config."""
from os.path import exists

import xdg

CUSTOM_TAG = "# CUSTOM - Add custom or override config below this line"

KITTY_CONFIG_FILE = f"{xdg.XDG_CONFIG_HOME}/kitty/kitty.conf"
KITTY_CONFIG_TEMPLATE = "configs/kitty.conf"

def write(data, file):
    for key, value in data.items():
        file.write(f"{key} {value}\n")

def translate(config):
    """Translate the @config to Kitty config."""
    terminal_config = config["terminal"]

    

    with open(KITTY_CONFIG_TEMPLATE, "r") as file:
        default_config = file.read()

    # Loading custom config created by user
    custom_user_config = ""
    if exists(KITTY_CONFIG_FILE):
        with open(KITTY_CONFIG_FILE, "r") as file:
            current_config = file.read()
            if CUSTOM_TAG in current_config:
                custom_user_config = current_config.split(CUSTOM_TAG)[1]

    with open(KITTY_CONFIG_FILE, "w+") as file:
        file.write(default_config)
        write(terminal_config["fonts"], file)
        write(terminal_config["cursor"], file)
        write(terminal_config["color"], file)
        file.write(CUSTOM_TAG)
        if custom_user_config:
            file.write(custom_user_config)