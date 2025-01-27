"""
command_manager.py

This module defines the CommandManager class, which is responsible for managing commands, subcommands, arguments, and flags for a command-line tool.

Classes:
    CommandManager: Manages commands, subcommands, arguments, and flags.

Functions:
    __init__(self): Initializes the CommandManager with an empty command dictionary.
    init(self): Initializes the CommandManager with predefined commands, arguments, and flags.
    add_command(self, command_name, description): Adds a new command to the command dictionary.
    add_argument_to_command(self, command_name, argument_name): Adds an argument to a command.
    add_flag_to_command(self, command_name, flag_name, description, flag_type): Adds a flag to a command.
    add_sub_command_to_command(self, command_name, sub_command_name, description): Adds a subcommand to a command.
    add_argument_to_sub_command(self, command_name, sub_command_name, argument_name): Adds an argument to a subcommand.
    add_flag_to_sub_command(self, command_name, sub_command_name, flag_name, description, flag_type): Adds a flag to a subcommand.
    save_commands(self): Saves the commands to a file in JSON format.

Author: cnoxlof
Date: 26/01/2025
Version: 1.0
Last update: 26/01/2025
"""

import json


class CommandManager:
    def __init__(self):
        self.commands = {}
        self.ready = False
        
    def load_commands(self):
        self.add_command("monitor","Monitor system metrics or tool usage in real-time.")

        self.add_argument_to_command('monitor', 'target')

        self.add_flag_to_command('monitor', '--interval', 'Set the update interval in seconds', 'integer')
        self.add_flag_to_command('monitor', '--log', 'Save the monitoring output to a file', 'string')
        self.add_flag_to_command('monitor', '--verbose', 'Display detailed metrics', 'boolean')


        self.add_sub_command_to_command('monitor', 'test', 'Test the integrity of the monitor command')
        self.add_argument_to_sub_command('monitor', 'test', 'target')

        self.add_flag_to_sub_command('monitor', 'test', '--interval', 'Set the update interval in seconds', 'integer')
        self.add_flag_to_sub_command('monitor','test', '--log', 'Save the monitoring output to a file', 'string')
        self.add_flag_to_sub_command('monitor', 'test','--verbose', 'Display detailed metrics', 'boolean')
        
        self.save_commands()
        
        self.ready = True
        


    def save_commands(self, debug=True):
        with open('data/commands.json', 'w') as file:
            file.flush()
            file.write(json.dumps(self.commands, indent=4))


    def add_command(self,command_name,command_description):
        if command_name in self.commands:
            print(f'command {command_name} already exist')
            return
        self.commands[command_name] = {'description': command_description, 'flags': {}, 'arguments' : [],'subcommands' : {}}




    def add_flag_to_command(self,command_name,flag_name,flag_description, flag_type):
        try:
            if not flag_name in self.commands[command_name]["flags"]:
                        self.commands[command_name]["flags"][flag_name] = {'description': flag_description, 'type' : flag_type}
            else:
                print(f'argument {flag_name} already exist')
        
        except KeyError as e:
            print(f"{e.args[0]} not found")
        
        
        



    def add_argument_to_command(self,command_name, argument_name):
        try:
            if not argument_name in self.commands[command_name]['arguments']:
                self.commands[command_name]['arguments'].append(argument_name) 
            else:
                print(f'argument {argument_name} already exist')
        
        except KeyError as e:
            print(f"{e.args[0]} not found")
        
        




    def add_sub_command_to_command(self,command_name, sub_command_name, sub_command_description):
        try:
            if not command_name in self.commands[command_name]['subcommands']:
                self.commands[command_name]['subcommands'][sub_command_name] = {'description': sub_command_description, 'flags': {},'arguments': []}
            else:
                print(f'subcommand {sub_command_name} already exist')
        except KeyError as e:
            print(f"{e.args[0]} not found")

        
        


    def add_flag_to_sub_command(self,command_name, sub_command_name,flag_name,flag_description, flag_type):
        try:
            subcommand = self.commands[command_name]['subcommands'][sub_command_name]
            subcommand['flags'][flag_name] = {"description": flag_description, "type": flag_type} 
        except KeyError as e:
            print(f"{e.args[0]} not found")
        

    def add_argument_to_sub_command(self,command_name, sub_command_name, argument_name):
        try:
            subcommand = self.commands[command_name]['subcommands'][sub_command_name]
            subcommand['arguments'].append(argument_name)
        except KeyError as e:
            print(f"{e.args[0]} not found")
        
