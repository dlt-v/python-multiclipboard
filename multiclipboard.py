import sys
import clipboard
import json


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


def list_clips(clips):
    for i, (key, clip) in enumerate(clips.items()):
        print(f'{i}.\t {key}:\t"{clip}"')


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
            list_clips(clips)

        case _:
            print(f'{bcolors.WARNING}Error: Unknown argument.{bcolors.ENDC}')

else:
    print(f'{bcolors.WARNING}Invalid data.{bcolors.ENDC} - {bcolors.COMMENT}Please check the number of arguments.{bcolors.ENDC}')
