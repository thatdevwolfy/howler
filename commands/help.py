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
