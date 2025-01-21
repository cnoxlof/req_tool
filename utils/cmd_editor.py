commands = {}

def add_command(name, params=[], help_text=""):
    commands[name] = {"data": {"help" : help_text}, "params": params}



def get_command():
    return commands


def add_sub_comand(name, sub_name, params=[], help_text=""):
    if name not in commands:
           commands[name] = {"data": {"help" : help_text}, "params": params}
    
    if "sub_commands" not in commands[name]:
        commands[name]["sub_commands"] = {}
        commands[name]["sub_commands"][sub_name] = sub_name
    






def add_param(command_name  ,param_name, param_type=str, required=False, help_text="", default=None, choices=None):
    param = {
        "name": param_name,
        "type": param_type,
        "required": required,
        "help": help_text,
        "default": default,
        "choices": choices
    }
    if command_name not in commands:
        commands[command_name] = []
    commands[command_name]["params"].append(param)


