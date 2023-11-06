import argparse

from drinker_thinker.src.config.config import Configs
from drinker_thinker.src.context_manager import ContextManager
from drinker_thinker.src.interactive.main_menu import MainMenu

def main():

    parser = argparse.ArgumentParser(description= 'default parser')
    parser.add_argument('--config_file', help='the configuration file')
    args = parser.parse_args()

    configs = Configs(args.config_file)
    context_manager = ContextManager(configs)
    main_menu = MainMenu(context_manager)
    main_menu.main_loop()

if __name__ == '__main__':
    main()
