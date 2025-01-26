from command_manager import CommandManager


RUN = True

def draw_logo():
    with open("assets/_logo.txt","r", encoding="utf-8") as data:
        print(data.read(), "\n")
        

        
        
        
def main():
    commandManager = CommandManager()
    commandManager.init()
    
    if commandManager.ready:
        print("Command Manager Ready")
    else:
        print("\x1b[31;1mError : \x1b[39;49;0mCommand Manager not ready")
        return
        
    
    input('press enter to continue')
    print("\033[H\033[J", end="")
    
    
    
    while RUN:
        draw_logo()
        input('> ')
        
        
if __name__ == "__main__":
    main()
    