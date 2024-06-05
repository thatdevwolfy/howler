import nextcord
from config import config
from nextcord.ext import commands
from Howler import Handler
client = commands.Bot(command_prefix="b",intents=nextcord.Intents.all())
handler = Handler(client,
                         commandFolder=config["handler"]["commandFolder"],
                         eventFolder=config["handler"]["eventFolder"],
                         useDefaultReadyEvent=config["handler"]["useDefaultOnReadyEvent"],
                         presence=config["handler"]["presence"],
                         status=config["handler"]["status"]
                         )
client.run(config["token"])