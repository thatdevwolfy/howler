import nextcord

config = {
    "handler": {
        "commandFolder": "commands", # Folder your commands are in
        "eventFolder": "events", # Folder your events are in
        "useDefaultOnReadyEvent": True, # Change this to false if your using your own on_ready event,
        "logfile": "logs", # Where the bot logs errors, command loading etc
        "presence": nextcord.Status, # .dnd/.online/.afk/.offline
        "status": nextcord.Game("With wolfhandler") # Set this to your status. Eg nextcord.watching/
    },
    "token": "" # Discord bot token (get it from https://discord.com/developers)
}