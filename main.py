import nextcord
from nextcord.ext import commands
from wolfhandler import CommandHandler
client = commands.Bot(command_prefix="b",intents=nextcord.Intents.all())
handler = CommandHandler(client,commandFolder="commands",eventFolder="events")
client.run("MTI0NTQ2NTM4NjQ1NjA2MDA1NA.GMBUXm.Cokr9T7d-_nVmuqjjNTa0LjEQtOP33vUe3Ndes")