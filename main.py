from command_manager import CommandManager
from command_parser import CommandParser
from utils.debugs_logs import *

RUN = True

def draw_logo():
    with open("assets/_logo.txt","r", encoding="utf-8") as data:
        print(data.read(), "\n")
        

        
        
        
def main():
    debug("This is a development version and is currently in debug mode.")
    
    
    commandManager = CommandManager()
    commandManager.load_commands()
    
    
    
    if commandManager.ready:
        success("Command Manager Ready")

    else:
        error("Command Manager not ready")
        return
    
    commandParser = CommandParser()
    
    if commandParser.ready:
        success("Command Manager Ready")
    else:
        error("Command Manager not ready")
        return
    

    
    
    input('press enter to continue')
    
    print("\033[H\033[J", end="")
    draw_logo()
    
    while RUN:
        
        data = input('> ')
        
        print(commandParser.parse_command(data))
        
        
        
        
if __name__ == "__main__":
    main()
    