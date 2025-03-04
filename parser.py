from utils.logging import error_log, success_log
from utils.cmd_editor import get_command

from commands.cmds_sys import main_cmd











def command_exists(data):
    commands = get_command()
    return data.split(' ')[0] in commands



def parse_command(data):
    commands = get_command()
    
    data = data.split(' ') # Split the data into a list
    data = list(filter(None, data)) # Remove empty spaces

    command = data[0]

    requiredParams = []

    # Check if the command have the right subcommand  
    if command in commands:
        print('sub_commands' in commands[command])
        if 'sub_commands' in commands[command]:
            if len(data) >= 2:
                if data[1] not in commands[command]['sub_commands']:
                    return error_log(f'Invalid Subcommand {data[1]}')
            else:
                return error_log(f'A subcommand is missing')
    else:
        return error_log(f'Invalid Command {command}')



    # Check if the command exists and if it has required parameters
    if len(commands[command]['params'])>=1:
        for param in commands[command]['params']:
            if param['required']:
                if param['name'] in data:
                    requiredParams.append(param['name'])
                else:
                    return error_log(f'A parameter is missing {param["name"]}')
            
    # Check if all the parameters are valid
    if len(commands[command]['params'])>=1:
        for param in data:
            if param[0] == '-':
                for param in commands[command]['params']:
                    if param['name'] == param:
                        return error_log(f'Invalid Parameter {param}')

    # Check if the required parameters are present
    for param in commands[command]['params']:
        if param['required'] and param['name'] not in requiredParams:
            return error_log(f'A parameter is missing {param["name"]}')
        
    # Check if the parameters have values
    for param in commands[command]['params']:
        if param['name'] in data:
            try:
                if data[data.index(param['name'])+1] == '':
                    return error_log(f'No Value for {param["name"]}')
            except IndexError:
                return error_log(f'No Value for {param["name"]}')
        else:
            if param['required']:
                return error_log(f'A parameter is missing {param["name"]}')

    # Check if the parameters have the correct types
    
    for param in commands[command]['params']:
        if param['name'] in data:
            try:
                if param['type'] == int:
                    int(data[data.index(param['name'])+1])
                elif param['type'] == bool:
                    if data[data.index(param['name'])+1] not in ['True', 'False']:
                        return error_log(f'Invalid Value for {param["name"]}, expected types {param["type"]}') 
                elif param['type'] == str:
                    pass
                else:
                    return error_log(f'Invalid Value for {param["name"]}, expected types {param["type"]}')
            except ValueError:
                return error_log(f'Invalid Value for {param["name"]}, expected types {param["type"]}')
        else:
            if param['required']:
                return error_log(f'A parameter is missing {param["name"]}')


    # Check if the parameters have the correct choices

    for param in commands[command]['params']:
        if param['name'] in data:
            if param['choices'] != None:
                if data[data.index(param['name'])+1] not in param['choices']:
                    return error_log(f'Invalid Value for {param["name"]}, Expected values are {param["choices"]}')
        else:
            if param['required']:
                return error_log(f'A parameter is missing {param["name"]}')

    main_cmd(data)
