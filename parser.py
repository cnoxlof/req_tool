
commands = {}

def add_command(name, params=[]):
    commands[name] = params











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
    commands[command_name].append(param)

# Adding a command with parameters
add_command('start', [])
add_param('start', '--timeout', param_type=int, required=True, help_text="The timeout value in seconds", default=30)
add_param('start', '--verbose', param_type=bool, required=True, help_text="Enable verbose output", default=False)
add_param('start', '--mode', param_type=str, required=False, help_text="Mode of operation", choices=["fast", "normal", "slow"])





def error_log(text):
    print('\033[31;40;1mError :\033[39;49;0m ' + text)
    
def warning_log(text):
    print('\033[33;40;1mWarning :\033[39;49;0m ' + text)
    
def succes_log(text):
    print('\033[32;40;1mSucces :\033[39;49;0m ' + text)



def command_exists(data):
    return data.split(' ')[0] in commands



def parse_command(data):
    data = data.split(' ')
    command = data[0]

    paramCheck = []

    for i in range(len(commands[command])):
        param = commands[command][i]
   


        if param['required']:
            if param['name'] in data:
                paramCheck.append(param['name'])
                
                

            else:
                return error_log(f'A parameter is missing {param['name']}')




    for i in range(len(commands[command])):
        if commands[command][i]["required"]:
            if not commands[command][i]['name'] in paramCheck:
                return f'A Paremeter is missing {commands[command][i]["name"]}'    

    succes_log('Everything Worked')

        
    # if param['type'] != None:
    #     return f'Starting with {param['name']} = {data[data.index(param['name'])+1]}'
    # else:
    #     return f'No Parameter Value is Needed'