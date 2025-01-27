import json

class CommandParser:
    def __init__(self):
        self.ready = False
        self.commands = {}
        self.reload_commands()
        self.ready = True

    def reload_commands(self):
        with open('data/commands.json', 'r') as file:
            self.commands = json.load(file)


    def parse_command(self,command):



        
        command = command.split()

        main_command = command[0]





        if command[1] in self.commands[main_command]['subcommands']:
            sub_command = command[1]
        else:
            sub_command = None

        


        

        flags = []
        arguments = []

        for key, elem in enumerate(command):
            if elem.startswith("--") or elem.startswith("-"):
                if elem.rfind('=') != -1:
                    flags.append((elem[:elem.rfind('=')], elem[elem.rfind('=')+1:]))
                elif key + 1 < len(command) and command[key+1].startswith("-") == False:
                    
                    
                    
                    
                    
                    
                    if sub_command and self.commands[main_command]['subcommands'][sub_command]['flags'][elem]['type'] == "boolean":
                        flags.append((elem, True))
                        
                    elif self.commands[main_command]['flags'][elem]['type'] == "boolean":
                        flags.append((elem, True))
                    else:
                        
                        flags.append((elem, command[key+1]))
                            
                            
                    
                else:
                    flags.append((elem, None))
            

        if sub_command:
            
            args_num = len(self.commands[main_command]['subcommands'][sub_command]['arguments'])
            if args_num > 0:
                arguments = command[-args_num:]





        return main_command, sub_command, flags, arguments
    


def main():
    parser = CommandParser()
    parser.reload_commands()
    
    
    
    example_commands = [
        "monitor --interval 5 --log output.log --verbose target1",
        "monitor --interval 10 target2",
        "monitor --log metrics.log target3",
        "monitor --verbose target4",
        "monitor test --interval 3 --log test_output.log --verbose target5",
        "monitor test --interval 2 target6",
        "monitor test --log test_metrics.log target7",
        "monitor test --verbose target8"
    ]
    
    
    
    
    for i in range(len(example_commands)):
        main_command, sub_command, flags, arguments =parser.parse_command(example_commands[i])



        # print(f'Command: {example_commands[i]}')
        # print(f"Main Command: {main_command}")
        # print(f"Sub Command: {sub_command}")
        # print(f'Flags: {flags}')
        # print(f'Arguments: {arguments}')
        # print("\n")
        print([main_command,sub_command,flags,arguments])
    
            
    
