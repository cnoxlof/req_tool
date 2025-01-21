from utils.logging import error_log, success_log
from utils.cmd_editor import add_command, add_param, get_command
from commands import main_cmd


# Adding a command with parameters

add_command('help', [])
add_command('exit', [])

add_command('cls', [])
add_command('clear', [])

add_command('start', [])
add_param('start', '--timeout', param_type=int, required=True, help_text="The timeout value in seconds", default=30)
add_param('start', '--verbose', param_type=bool, required=True, help_text="Enable verbose output", default=False)
add_param('start', '--mode', param_type=str, required=False, help_text="Mode of operation", choices=["fast", "normal", "slow"])


commands = get_command()



def command_exists(data):
    return data.split(' ')[0] in commands



def parse_command(data):
    data = data.split(' ') # Split the data into a list
    data = list(filter(None, data)) # Remove empty spaces

    command = data[0]

    requiredParams = []

    # Check if the command exists and if it has required parameters
    for param in commands[command]:
        if param['required']:
            if param['name'] in data:
                requiredParams.append(param['name'])
            else:
                return error_log(f'A parameter is missing {param["name"]}')
            
    # Check if all the parameters are valid
    for param in data:
        if param[0] == '-':
            if param not in [param['name'] for param in commands[command]]:
                return error_log(f'Invalid Parameter {param}')

    # Check if the required parameters are present
    for param in commands[command]:
        if param['required'] and param['name'] not in requiredParams:
            return error_log(f'A parameter is missing {param["name"]}')
        
    # Check if the parameters have values
    for param in commands[command]:
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
    
    for param in commands[command]:
        if param['name'] in data:
            try:
                if param['type'] == int:
                    int(data[data.index(param['name'])+1])
                elif param['type'] == bool:
                    if data[data.index(param['name'])+1] not in ['True', 'False']:
                        return error_log(f'Invalid Value for {param["name"]}')
                elif param['type'] == str:
                    pass
                else:
                    return error_log(f'Invalid Type for {param["name"]}')
            except ValueError:
                return error_log(f'Invalid Value for {param["name"]}')
        else:
            if param['required']:
                return error_log(f'A parameter is missing {param["name"]}')


    # Check if the parameters have the correct choices

    for param in commands[command]:
        if param['name'] in data:
            if param['choices'] != None:
                if data[data.index(param['name'])+1] not in param['choices']:
                    return error_log(f'Invalid Value for {param["name"]}, Expected values are {param["choices"]}')
        else:
            if param['required']:
                return error_log(f'A parameter is missing {param["name"]}')

    main_cmd(data)
