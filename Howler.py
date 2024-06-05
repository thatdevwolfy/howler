import os, importlib.util, nextcord, datetime
from nextcord.ext import commands
logo = """
*****************************************************
*██╗  ██╗ ██████╗ ██╗    ██╗██╗     ███████╗██████╗ *
*██║  ██║██╔═══██╗██║    ██║██║     ██╔════╝██╔══██╗*
*███████║██║   ██║██║ █╗ ██║██║     █████╗  ██████╔╝*
*██╔══██║██║   ██║██║███╗██║██║     ██╔══╝  ██╔══██╗*
*██║  ██║╚██████╔╝╚███╔███╔╝███████╗███████╗██║  ██║*
*╚═╝  ╚═╝ ╚═════╝  ╚══╝╚══╝ ╚══════╝╚══════╝╚═╝  ╚═╝*
*****************************************************"""
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
        if useDefaultReadyEvent == True:
            @self.client.event
            async def on_ready(): # Default on_ready event if flag useDefaultReadyEvent is True
                os.system("clear" if os.name != "nt" else "cls")
                string = ""
                for item in commandsThatErrored:
                    string = f"{string}{item}"
                print(f"""{logo}\nLogged in as {client.user}\nGuilds: {len(client.guilds)} \nCommands failed to load ({len(commandsThatErrored)}): {string}""")
                self.raiseLog(f"{logo}\nLogged in as {client.user}")
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
                print(f"Failed to load command: {command['name']}")
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
        self.client.loop.create_task(self.set_presence())
    async def set_presence(self):
        await self.client.wait_until_ready()
        await self.client.change_presence(status=self.presence, activity=self.status)