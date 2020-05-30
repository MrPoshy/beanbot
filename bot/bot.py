# bot.py
# BeanBot Main
import os

import discord
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

# Create connection
client = discord.Client()

@client.event
async def on_ready():
    # Connect to all guilds
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is in!\n'
        f'Connected to: {guild.name}(id: {guild.id})'
    )

client.run(TOKEN)
