import discord
import os
import random
from dotenv import load_dotenv

token = os.getenv("token")
intents = discord.Intents(messages=True, message_content=True)
client = discord.Client()

