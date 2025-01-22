# Command Parser

This script parses command-line commands into their main command, subcommand, flags, and arguments.

## Example

Given the command: `mytool deploy --server=192.168.1.1 --user=admin --port=22 --key=~/.ssh/id_rsa production`

The script will output:

Command: mytool deploy --server=192.168.1.1 --user=admin --port=22 --key=<del>/.ssh/id_rsa production Main Command: mytool Sub Command: deploy Flags: [('--server', '192.168.1.1'), ('--user', 'admin'), ('--port', '22'), ('--key', '</del>/.ssh/id_rsa')] Arguments: ['production']

## Usage

1. Ensure you have Python installed on your system.
2. Clone this repository or download the script.
3. Place your commands in the `example_commands` list in the script.
4. Run the script using the command:
    ```sh
    python main.py
    ```

## Script Details

The script contains the following functions:

- `parse_command(command)`: Parses a command string into its main command, subcommand, flags, and arguments.
- `main()`: Iterates over the `example_commands` list, parses each command, and prints the results.

## Example Commands

You can modify the `example_commands` list in the script to include your own commands for parsing.

```python
example_commands = [
    "mytool deploy --server=192.168.1.1 --user=admin --port=22 --key=~/.ssh/id_rsa production",
    "mytool run --config=config.yaml file.txt",
    "admin reset --force",
    # Add more commands here
]