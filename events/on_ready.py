# events/on_ready.py
import os


async def on_ready():
    print("Logged in.")

export = {
    "name": "on_ready",
    "execution": on_ready
}
