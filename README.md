## Howler: A Nextcord Command Handler

Howler is a versatile Discord.py command handler designed to add wolf-themed functionality to your bot. It allows you to interact with users through commands and events related to wolves.

### Features

* **Modular Design:** Howler is built with modularity in mind, making it easy to extend with new functionalities.
* **Customizable:** You can easily configure Howler to respond to specific commands and events.

### Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/thatdevwolfy/howler
   ```

2. **Install Dependencies:**

   Navigate to the project directory and install the required libraries using pip:

   ```bash
   pip install nextcord 
   ```

### Usage

**1. Example:**
```py
import nextcord
from config import config
from nextcord.ext import commands
from Howler import Handler
client = commands.Bot(command_prefix="(prefix)",intents=nextcord.Intents.all())
handler = Handler(client,
                         commandFolder=config["handler"]["commandFolder"],
                         eventFolder=config["handler"]["eventFolder"],
                         useDefaultReadyEvent=config["handler"]["useDefaultOnReadyEvent"],
                         presence=config["handler"]["presence"],
                         status=config["handler"]["status"]
                         )
client.run(config["token"])
```

**3. Define Commands and Events:**

Howler allows you to define custom commands and event handlers. Here's a basic example:

```python
# commands/example_command.py
from Howler import load_modules
import nextcord
async def help(ctx, filter=""):
    commands = load_modules("commands")
    embed = nextcord.Embed(title="Commands")
    for i in commands:
        if filter != "":
            if i["name"] == filter:
                embed.add_field(name=i["name"],value=i["description"])
        else:
            embed.add_field(name=i["name"],value=f'{i["description"]} - {i["aliases"] or ""}')
    await ctx.reply(embed=embed)

export = {
    "name": "help",
    "description": "get help",
}

# events/on_ready.py
import os


async def on_ready():
    print("Logged in.")

export = {
    "name": "on_ready",
    "execution": on_ready
}

```


**4. Load your config**

```py
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
}```
**5. Register Howler with the Client:**

```python

client.run("your_bot_token")
```

### Extending Howler

Howler provides a foundation for building commands and events. You can create new modules or cogs to handle specific howling good interactions (e.g., games, image sharing, role management).

### Contributing

We welcome contributions to improve Howler! Feel free to submit pull requests with new features, bug fixes, or improvements.

### License

Howler is licensed under the MIT License (see LICENSE file for details).
