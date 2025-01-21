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
    print(f"        └ \033[1;34mParameters: \033[1;32m{param['name']}\033[0m")
    print(f"          ├ \033[0;36mType:\033[0m  {param['type']}")
    print(f"          ├ \033[0;36mRequired:\033[0m  {param['required']}")
    print(f"          ├ \033[0;36mHelp:\033[0m  {param['help']}")
    print(f"          ├ \033[0;36mDefault:\033[0m  {param['default']}")
    print(f"          └ \033[0;36mChoices:\033[0m  {param['choices']}")

def help(cmd_str):
    if len(cmd_str) == 1:
        for elem in get_command():
            info_log(f"\033[33;49;1m{elem.upper()} \033[39;49;0mCommand : ")
            print(f"        \033[0;36mDescription:\033[0m {get_command()[elem]['data']['help']}")
            for param in get_command()[elem]["params"]:
                help_display(param)

    elif len(cmd_str) == 2:
        if not cmd_str[1] in get_command():
            error_log("Command not found")
            return 

        elem = cmd_str[1]
        info_log(f"\033[33;49;1m{elem.upper()} \033[39;49;0mCommand : ")
        print(f"        \033[0;36mDescription:\033[0m {get_command()[elem]['data']['help']}")
        for param in get_command()[elem]["params"]:
            help_display(param)
            
    else:
        error_log("To many Arguments")
