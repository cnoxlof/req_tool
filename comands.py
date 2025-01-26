commands = {
    "mytool": {
        "description": "Main tool command.",
        "flags": {
            "-h": {"description": "Display help information", "type": "boolean"},
            "--version": {"description": "Display the tool version", "type": "boolean"},
        },
        "subcommands": {
            "run": {
                "description": "Run the tool.",
                "flags": {
                    "-v": {"description": "Verbose output", "type": "boolean"},
                    "--config": {"description": "Path to config file", "type": "string"},
                    "--threads": {"description": "Number of threads to use", "type": "integer"},
                    "--dry-run": {"description": "Simulate the run without making changes", "type": "boolean"},
                },
                "arguments": ["file"],
            },
            "build": {
                "description": "Build the tool.",
                "flags": {
                    "--debug": {"description": "Enable debug mode", "type": "boolean"},
                    "--output": {"description": "Specify output directory", "type": "string"},
                },
                "arguments": ["source", "destination"],
            },
            "test": {
                "description": "Run tests on the tool.",
                "flags": {
                    "--all": {"description": "Run all tests", "type": "boolean"},
                    "--filter": {"description": "Filter tests by keyword", "type": "string"},
                    "--timeout": {"description": "Set a timeout for tests", "type": "integer"},
                },
                "arguments": [],
            },
            "deploy": {
                "description": "Deploy the tool to a server.",
                "flags": {
                    "--server": {"description": "Target server address", "type": "string"},
                    "--user": {"description": "Username for deployment", "type": "string"},
                    "--port": {"description": "Server port", "type": "integer"},
                    "--key": {"description": "Path to SSH key", "type": "string"},
                },
                "arguments": ["environment"],
            },
        },
    },
    "admin": {
        "description": "Administrative commands.",
        "subcommands": {
            "reset": {
                "description": "Reset the tool configuration.",
                "flags": {
                    "--force": {"description": "Force reset without confirmation", "type": "boolean"},
                },
                "arguments": [],
            },
            "status": {
                "description": "Check the tool's status.",
                "flags": {
                    "--json": {"description": "Output status in JSON format", "type": "boolean"},
                },
                "arguments": [],
            },
        },
    },
}

example_commands = [
    "mytool -h",
    "mytool --version",
    "mytool run -v file.txt",
    "mytool run --config=config.yaml file.txt",
    "mytool run --threads=4 --dry-run file.txt",
    "mytool build source/ dest/",
    "mytool build --debug source/ dest/",
    "mytool build --output=build/ source/ dest/",
    "mytool test --all",
    "mytool test --filter=unit_tests",
    "mytool test --timeout=60",
    "mytool deploy production",
    "mytool deploy --server=192.168.1.1 --user=admin --port=22 --key=~/.ssh/id_rsa production",
    "admin reset",
    "admin reset --force",
    "admin status",
    "admin status --json",
]