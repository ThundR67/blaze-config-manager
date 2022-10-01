"""Translated Blaze config to Kitty config."""
import xdg

def write(data, file):
    for key, value in data.items():
        file.write(f"{key} {value}\n")

def translate(config):
    """Translate the @config to Kitty config."""
    kitty_config = f"{xdg.XDG_CONFIG_HOME}/kitty/kitty.conf"
    terminal_config = config["terminal"]

    with open("configs/kitty.conf", "r") as file:
        default_config = file.read()
    
    with open(kitty_config, "w+") as file:
        file.write(default_config)
        write(terminal_config["fonts"], file)
        write(terminal_config["cursor"], file)
        write(terminal_config["color"], file)