# events/on_ready.py
import os


async def messageHandler(message):
    print(f"{message}")
export = {
    "name": "on_message",
    "execution": messageHandler
}
