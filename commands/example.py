# commands/example_command.py
async def example_command(ctx):
    await ctx.send("Hello, world!")

export = {
    "name": "example",
    "description": "An example command",
    "execution": example_command
}
