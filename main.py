from parser import parse_command, command_exists



def clear():
    print("\033[H\033[J", end="")
    draw_logo()
    


def draw_logo():
    with open("./assets/_logo.txt", "r", encoding='utf-8') as file:
        print(file.read(), end="\n\n")


draw_logo()
run = True

while run:
    cmd_string = str(input("> "))
    cmd_list = cmd_string.split()


    if cmd_string == 'exit':
        run = False


    elif command_exists(cmd_string):
        parse_command(cmd_string)

    else:
        print(f"\033[31;40;1mError: \033[37;49;0mUnknown command: '{cmd_list[0]}'. \033[39;49;0mType 'help' for a list of available commands.\033[37;49;0m")
