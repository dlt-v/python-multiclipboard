import sys
import clipboard
import json
import os


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[31m'
    COMMENT = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


CACHE_PATH = "clipboard.json"

AVAILABLE_COMMANDS = {
    "help": 'See available commands.',
    "save": 'Save content to multiclipboard.',
    "load": 'Copy content to your clipboard.',
    "list": 'Show all currently saved clips.',
    "clear": 'Clear out all clips.'
}


def save_clips(filepath, data):
    with open(filepath, "w") as f:
        json.dump(data, f)


def read_clips(filepath):
    try:
        with open(filepath, "r") as f:
            data = json.load(f)
            return data
    except:
        return {}


def list_data(data):
    if len(data) == 0:
        print(f'{bcolors.COMMENT}No saved clips.{bcolors.ENDC}')
    for i, (key, value) in enumerate(data.items()):
        print(
            f'{bcolors.HEADER}{key}{bcolors.ENDC} {bcolors.OKBLUE}:{bcolors.ENDC} {value}')


def clear_clips():
    if os.path.exists(CACHE_PATH):
        os.remove(CACHE_PATH)


if len(sys.argv) == 2:
    command = sys.argv[1]
    clips = read_clips(CACHE_PATH)

    match command:

        case 'save':
            key = input("Enter a key: ")
            clips[key] = clipboard.paste()
            save_clips(CACHE_PATH, clips)
            print(f'{bcolors.OKBLUE}Clip saved!{bcolors.ENDC}')

        case 'load':
            key = input("Enter a key: ")
            if key in clips:
                clipboard.copy(clips[key])
                print(f'{bcolors.OKBLUE}Clip copied!{bcolors.ENDC}')
            else:
                print(f'{bcolors.WARNING}Error: Key does not exist.{bcolors.ENDC}')

        case 'list':

            list_data(clips)

        case 'clear':
            clips = {}
            clear_clips()
            print(f'{bcolors.OKBLUE}Clip file cleared!{bcolors.ENDC}')

        case 'help':
            print(f'{bcolors.COMMENT}Available commands:{bcolors.ENDC}')
            list_data(AVAILABLE_COMMANDS)

        case _:
            print(f'{bcolors.WARNING}Error: Unknown argument.{bcolors.ENDC}')

else:
    print(f'{bcolors.WARNING}Invalid data.{bcolors.ENDC} - {bcolors.COMMENT}Please check the number of arguments.{bcolors.ENDC}')
