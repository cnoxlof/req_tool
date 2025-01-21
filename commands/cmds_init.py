from utils.cmd_editor import *

def cmds_init():
    add_command('help', help_text="Display help for commands")
    add_command('exit', help_text="Exit the program")

    add_command('cls', help_text="Clear the screen")
    add_command('clear', help_text="Clear the screen")

    add_command('start', [], help_text="Start the program")
    add_param('start', '--timeout', param_type=int, required=True, help_text="The timeout value in seconds", default=30)
    add_param('start', '--verbose', param_type=bool, required=True, help_text="Enable verbose output", default=False)
    add_param('start', '--mode', param_type=str, required=False, help_text="Mode of operation", choices=["fast", "normal", "slow"])


    print(get_command())

    add_command('request', [], help_text="Send a request")
    add_param('request', '--url', param_type=str, required=True, help_text="The URL to send the request to")
    
    
    
    add_command('set', [], help_text=' Set global parameters for all requests (e.g., headers, base URL).')

