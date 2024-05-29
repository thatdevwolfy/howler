import os
import importlib.util
from nextcord.ext import commands
def load_modules(client, directory):
    for filename in os.listdir(directory):
        if filename.endswith(".py"):
            file_path = os.path.join(directory, filename)
            spec = importlib.util.spec_from_file_location(filename[:-3], file_path)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            yield module.export

class CommandHandler:
    def __init__(self, client, commandFolder="commands", eventFolder="events"):
        self.client = client
        self.eventFolder = eventFolder
        self.commandFolder = commandFolder

        # Load events

        for event in load_modules(client, f'./{eventFolder}'):
            event_handler = event["execution"]
            print(f'Loading Event: {event["name"]}')
            client.add_listener(event_handler, event["name"])

        # Load commands
        for command in load_modules(client, f'./{commandFolder}'):
            print(f"Loading Command: {command['name']}")
            client.add_command(commands.Command(command["execution"], name=command["name"], description=command["description"]))
