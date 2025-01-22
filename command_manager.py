import json


commands = {}



def add_command(command_name,command_description):
    if command_name in commands:
        print(f'command {command_name} already exist')
        return
    commands[command_name] = {'description': command_description, 'flags': {}, 'arguments' : [],'subcommands' : {}}




def add_flag_to_command(command_name,flag_name,flag_description, flag_type):
    if not command_name in commands:
        print("command not found")
        return




    if flag_name in commands[command_name]["flags"]:
        print(f'flags {flag_name} already exist')
        return
    
    commands[command_name]["flags"][flag_name] = {'description': flag_description, 'type' : flag_type}


def add_argument_to_command(command_name, argument_name):
    if not command_name in commands:
        print("command not found")
        return 
    
    if argument_name in commands[command_name]['arguments']:
        print(f'argument {argument_name} already exist') 
        return

    commands[command_name]['arguments'].append(argument_name) 
    




def add_sub_command_to_command(command_name, sub_command_name, sub_command_description):
    if not command_name in commands:
        print("command not found")
        return 
    
    if sub_command_name in commands[command_name]['subcommands']:
        print(f'subcommand {sub_command_name} already exist')
        return
    
    commands[command_name]['subcommands'][sub_command_name] = {'description': sub_command_description, 'flags': {},'arguments': []}


def add_flag_to_sub_command(command_name, sub_command_name,flag_name,flag_description, flag_type):
    if not command_name in commands:
        print("command not found")
        return 

    if not sub_command_name in commands[command_name]['subcommands']:
        print("subcommand not found")
        return   
    

    commands[command_name]['subcommands'][sub_command_name]['flags'][flag_name] = {"description": flag_description, "type": flag_type}







def add_argument_to_sub_command():
    pass



add_command("monitor","Monitor system metrics or tool usage in real-time.")

add_argument_to_command('monitor', 'target')

add_flag_to_command('monitor', '--interval', 'Set the update interval in seconds', 'integer')
add_flag_to_command('monitor', '--log', 'Save the monitoring output to a file', 'string')
add_flag_to_command('monitor', '--verbose', 'Display detailed metrics', 'boolean')


add_sub_command_to_command('monitor', 'test', 'Test the integrity of the monitor command')

add_flag_to_sub_command('monitor', 'test', '--interval', 'Set the update interval in seconds', 'integer')
add_flag_to_sub_command('monitor','test', '--log', 'Save the monitoring output to a file', 'string')
add_flag_to_sub_command('monitor', 'test','--verbose', 'Display detailed metrics', 'boolean')



with open('data.json', 'w')as file:
    file.flush()
    file.write(json.dumps(commands, indent=4))


print(json.dumps(commands, indent=4))

