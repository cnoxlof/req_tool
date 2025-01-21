from utils.logging import error_log, success_log, warning_log,info_log
from utils.cmd_editor import add_command, add_param, get_command




def main_cmd(cmd_str):
    if cmd_str[0] == "help":
        help(cmd_str)









def help(cmd_str):
    if len(cmd_str) == 1:
        cmds = []
        for cmd in get_command():
            cmds.append(cmd)
        info_log(f"Available Commands: {', '.join(cmds)}")
    elif len(cmd_str) == 2:
        success_log(f"Help for {cmd_str[1]}")
    else:
        error_log("To many Arguments")
