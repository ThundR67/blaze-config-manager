"""Main file."""
import sys
import yaml

import kitty_translator

def translate(filename):
    """Translate the @filename to respective applications' config files."""
    with open(filename, 'r') as file:
        config  = yaml.load(file, Loader=yaml.FullLoader)
        kitty_translator.translate(config)

if __name__ == "__main__":
    translate(sys.argv[1])