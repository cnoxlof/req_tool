from utils.logging import error_log, success_log, warning_log,info_log
from utils.cmd_editor import add_command, add_param, get_command




def main_cmd(cmd_str):
    cmd = cmd_str[0]
    
    if cmd == "help":
        help(cmd_str)
    elif cmd == "clear" or cmd == "cls":
        clear_cmd()


def clear_cmd():
    print("\033c")
    with open("./assets/_logo.txt", "r", encoding='utf-8') as file:
        print(file.read(), end="\n\n")
    



def help_display(param):
    print(f"        └ Parameter: {param['name']}")
    print(f"          ├ Type: {param['type']}")
    print(f"          ├ Required: {param['required']}")
    print(f"          ├ Help: {param['help']}")
    print(f"          ├ Default: {param['default']}")
    print(f"          └ Choices: {param['choices']}")



def help(cmd_str):

    if len(cmd_str) == 1:
        for elem in get_command():
            info_log(f"\033[39;49;1m{elem.upper()} \033[39;49;0mCommand : {get_command()[elem]['data']['help']}")
            for param in get_command()[elem]["params"]:
                help_display(param)

    elif len(cmd_str) == 2:
        elem = cmd_str[1]

        info_log(f"\033[39;49;1m{elem.upper()} \033[39;49;0mCommand : {get_command()[elem]['data']['help']}")
        for param in get_command()[elem]["params"]:
            help_display(param)


    else:
        error_log("To many Arguments")
