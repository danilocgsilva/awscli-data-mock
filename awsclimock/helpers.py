import sys

def get_command_to_mock() -> str:

    try:
        command = sys.argv[1]
    except IndexError:
        command = ask_command()

    return command


def ask_command():
    return input("Which AWS command do you wish to mock? Please, type the command name: ")