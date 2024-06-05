
## Howler: Unleash the Howling Power in Your Discord Pack!

Howler is a mighty Discord.py command handler, built with the spirit of the wolf in mind. It empowers you to create a thrilling, wolf-themed experience for your Discord server. Howler lets you interact with your pack through commands and events that celebrate all things wolf!

### Howling Features:

* **Modular by Pack:** Howler boasts a modular design, allowing you to effortlessly expand its features. Craft new functionalities to suit your pack's needs, keeping your server a constantly exciting hunting ground. 
* **Customizable Howls:** Make Howler truly your own! Configure it to respond to unique commands and events, creating a personalized experience for your pack members.

### Howling into Action: Getting Started

1. **Join the Pack:**

   ```bash
   git clone https://github.com/thatdevwolfy/howler
   ```

2. **Gather Your Supplies:**

   Navigate to the project directory and install the required libraries using pip:

   ```bash
   pip install nextcord
   ```

### Howling with Authority: Using Howler

**1. A Howling Example:**

```python
import nextcord
from config import config
from nextcord.ext import commands
from Howler import Handler

# Set up your alpha bot
client = commands.Bot(command_prefix="!", intents=nextcord.Intents.all())
handler = Handler(client,
                  commandFolder=config["handler"]["commandFolder"],
                  eventFolder=config["handler"]["eventFolder"],
                  useDefaultReadyEvent=config["handler"]["useDefaultOnReadyEvent"],
                  presence=config["handler"]["presence"],
                  status=config["handler"]["status"])

# Unleash the bot!
client.run(config["token"])
```

**2. Craft Howling Commands and Events:**

Howler lets you define custom commands and event handlers that resonate with your pack. Here's a basic example:

```python
# commands/example_command.py
from Howler import load_modules
import nextcord

async def help(ctx, filter=""):
  """Provides guidance on available commands for your pack."""
  commands = load_modules("commands")
  embed = nextcord.Embed(title="Pack Commands")
  for command in commands:
    if filter:
      if command["name"] == filter:
        embed.add_field(name=command["name"], value=command["description"])
    else:
      aliases = command.get("aliases", "")  # Handle optional aliases
      embed.add_field(name=command["name"], value=f"{command['description']} - {aliases}")
  await ctx.reply(embed=embed)

# Register the command
export = {
  "name": "help",
  "description": "Get help with available commands for your pack.",
}

# events/on_ready.py
async def on_ready():
  """Triggered when the bot is ready to howl."""
  print(f"Logged in as {client.user} (ID: {client.user.id})")

# Register the event
export = {
  "name": "on_ready",
  "execution": on_ready,
}
```

**3. Bind Howler to Your Alpha:**

```python
client.run("your_bot_token")  # Replace with your actual bot token
```

### Howling Beyond the Basics: Extending Howler

Howler is the foundation for your howlin' good adventures. Create new modules or cogs for functionalities like:

* **Image Sharing:** Unleash the majesty of wolves with image sharing features. 
* **Role Management:** Organize your pack with a robust role management system, like Alpha, Beta, Omega roles.

### Join the Howling Chorus: Contributing to Howler

We welcome all wolves who want to strengthen the pack! Feel free to submit pull requests for new features, bug fixes, or improvements. Let's make Howler the ultimate tool for a howling good time on Discord!

### Howling Openly: License

Howler is licensed under the MIT License (see LICENSE file for details). This allows for open collaboration and customization within your projects.
