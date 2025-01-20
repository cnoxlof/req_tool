import argparse

from parser import parse_command, command_exists



_logo = [
    '██████╗ ███████╗ ██████╗ ████████╗ ██████╗  ██████╗ ██╗     ',
    '██╔══██╗██╔════╝██╔═══██╗╚══██╔══╝██╔═══██╗██╔═══██╗██║     ',
    '██████╔╝█████╗  ██║   ██║   ██║   ██║   ██║██║   ██║██║     ',
    '██╔══██╗██╔══╝  ██║▄▄ ██║   ██║   ██║   ██║██║   ██║██║     ',
    '██║  ██║███████╗╚██████╔╝   ██║   ╚██████╔╝╚██████╔╝███████╗',
    '╚═╝  ╚═╝╚══════╝ ╚══▀▀═╝    ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝',
]

parser = argparse.ArgumentParser(description="A simple command-line parser")
parser.add_argument("-n", "--name", type=str, help="Your name", required=True)
parser.add_argument("-a", "--age", type=int, help="Your age", required=True)
parser.add_argument("-v", "--verbose", action="store_true", help="Enable verbose mode")



def draw_logo():
    for row in _logo:
        print(row)
    print()






draw_logo()
run = True

while run:
    cmd_string = str(input("> "))
    cmd_list = cmd_string.split()



    
    if command_exists(cmd_string):
        parse_command(cmd_string)


    elif cmd_string == 'cls' or cmd_string == 'clear':
        print("\033[H\033[J", end="")
        draw_logo()

    elif cmd_string == 'exit':
        run = False

    else:
        print(f"\033[31;40;1mError: \033[37;49;0mUnknown command: '{cmd_list[0]}'. \033[39;49;0mType 'help' for a list of available commands.\033[37;49;0m")
