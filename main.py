
from comands import example_commands, commands



def parse_command(command):
    command = command.split()

    main_command = command[0]

    if command[1] in commands[main_command]['subcommands']:
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
                flags.append((elem, command[key+1]))
            else:
                flags.append((elem, None))
        

    if sub_command:
        args_num = len(commands[main_command]['subcommands'][sub_command]['arguments'])
        if args_num > 0:
            arguments = command[-args_num:]





    return main_command, sub_command, flags, arguments
    



def main():
    for i in range(len(example_commands)):
        main_command, sub_command, flags, arguments = parse_command(example_commands[i])

        print(f'Command: {example_commands[i]}')
        print(f"Main Command: {main_command}")
        print(f"Sub Command: {sub_command}")
        print(f'Flags: {flags}')
        print(f'Arguments: {arguments}')
        print("\n\n")
    
            
    



if __name__ == "__main__":
    main()