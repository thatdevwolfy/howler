import os, importlib.util, nextcord, datetime, time, psutil, sys
from nextcord.ext import commands
startTime = time.time()
def get_memory_usage():
  """Gets the current memory usage of the Python process in MB."""
  mem = psutil.Process().memory_info().rss / 1024**2  # Convert bytes to MB
  return f"{mem:.2f} MB"
logo = """
*****************************************************
*██╗  ██╗ ██████╗ ██╗    ██╗██╗     ███████╗██████╗ *
*██║  ██║██╔═══██╗██║    ██║██║     ██╔════╝██╔══██╗*
*███████║██║   ██║██║ █╗ ██║██║     █████╗  ██████╔╝*
*██╔══██║██║   ██║██║███╗██║██║     ██╔══╝  ██╔══██╗*
*██║  ██║╚██████╔╝╚███╔███╔╝███████╗███████╗██║  ██║*
*╚═╝  ╚═╝ ╚═════╝  ╚══╝╚══╝ ╚══════╝╚══════╝╚═╝  ╚═╝*
*****************************************************
"""
def load_modules(directory):
    for filename in os.listdir(directory):
        if filename.endswith(".py"):
            file_path = os.path.join(directory, filename)
            spec = importlib.util.spec_from_file_location(filename[:-3], file_path)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            yield module.export
class Handler:
    def raiseLog(self, log):
        with open(self.logfile,"a") as p: p.write(f"\n{datetime.datetime.now()}: {log}") # Logging event happening/loading
    def raiseError(self, error):
        with open(self.logfile, "a") as p: p.write(f"\n{datetime.datetime.now()}: {error}") # Logging errors
    def __init__(self, client, commandFolder="commands", eventFolder="events",presence=nextcord.Status.dnd,status=nextcord.Game(name="github.com/thatdevwolfy/howler"),logfile="logs",useDefaultReadyEvent=True):
        self.client = client; self.presence = presence; self.status = status; self.logfile = logfile; self.eventFolder = eventFolder; self.commandFolder = commandFolder
        commandsThatErrored = []
        loadedCommands = []
        if useDefaultReadyEvent == True:
            @client.event
            async def on_ready():
                """Enhanced on_ready event with informative output and logging."""
                os.system("clear" if os.name != "nt" else "cls")
                print(f"{logo}\nClient Information:")
                print(f"- Logged in as: {client.user} ({client.user.id})")
                print(f"- Guilds: {len(client.guilds)}")
                print(f"- Users: {len(client.users)}")  # Added User Count
                print(f"- Latency: {round(client.latency * 1000)}ms")
                print(f"- Launch time: {str(round(startTime,0) - round(time.time(),0)).replace('-','')}s")
                print("\nCommand Status:")
                print(f"- Successfully Loaded: {len(loadedCommands)} commands")
                if commandsThatErrored:
                    print(f"- Failed to Load ({len(commandsThatErrored)}):")
                    for command in commandsThatErrored:
                        print(f"  - {command}")  # More detailed error handling
                else:
                    print("- No errors encountered during command loading.")
                print("\nAdditional Information:")
                print(f"- Memory Usage: {get_memory_usage()}")
        os.system("clear" if os.name != "nt" else "cls")
        print(f"{logo}")
        for event in load_modules(f'./{eventFolder}'):
            event_handler = event["execution"]
            if useDefaultReadyEvent != False:
                if event["name"] == "on_ready": 
                    self.raiseLog("Wolfhandler already comes with a built in on_ready event. if you wish to use your own please set useDefaultOnReadyEvent in your config to false")
                continue
            print(f'Loading Event: {event["name"]}')
            self.raiseLog(f"Loaded {event['name']}")
            client.add_listener(event_handler, event["name"]) # Load Events
        for command in load_modules(f'./{commandFolder}'):      
            try:
                x = command["execution"]
            except:
                print(f"{error}\nFailed to load command: {command['name']}")
                commandsThatErrored.append(command["name"])
                self.raiseError(f"Failed to load {command['name']} as it doesnt have the execution function")
                continue
            if command["name"] == "help":
                client.remove_command("help")
            try:
                if command["aliases"]:
                    client.add_command(commands.Command(command["execution"], name=command["name"], description=command["description"],aliases=command["aliases"])) # Add command to bot with alliases
            except:
                self.raiseError(f"Unexpected Error when loading {command['name']}: Command does not have any allias, loading without alliases")
            else:
                client.add_command(commands.Command(command["execution"], name=command["name"], description=command["description"])) # Add command to bot without alliases
                self.raiseLog(f"Loaded {command['name']}")
            loadedCommands.append(command["name"])
        self.client.loop.create_task(self.set_presence())
    async def set_presence(self):
        await self.client.wait_until_ready()
        await self.client.change_presence(status=self.presence, activity=self.status)