# bot.py
# BeanBot Main
import os
import random
import asyncio

import discord
from discord.ext import commands
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

# Create connection
bot = commands.Bot(command_prefix="B>")

@bot.event
async def on_ready():
    # Connect to all guilds
    for guild in bot.guilds:
        if guild.name == GUILD:
            break 
    print(
        f'{bot.user} is in!\n'
        f'Connected to: {guild.name}(id: {guild.id})'
    )

# Logan Sounds
class LoganSounds(commands.Cog):
    @bot.command(name='LoganSounds', description='Play some epic logan sounds', pass_context=True, aliases=['log', 'logan', 'Logan'])
    async def playsound(ctx):
        channel = ctx.message.author.voice.channel

        # channel check
        if not channel:
            await ctx.send('You ain\'t in a channel homie')
            return
        
        # channel info
        await ctx.send('Playing')
        voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
        if voice and voice.is_connected():
            await voice.move_to(channel)
        else:
            voice = await channel.connect()
        
        source = discord.FFmpegPCMAudio('/home/bot-man/beanbot/sound/logan/' + random.choice(os.listdir('/home/bot-man/beanbot/sound/logan')))
        player = voice.play(source)

        # create stream
        while voice.is_playing():
            await asyncio.sleep(1)

        # disconnect when done
        voice.stop()
        await voice.disconnect()


# Message events
@bot.event
async def on_message(message):
    if message.author == bot.user or message.author.bot:
        return

    if discord.utils.get(message.author.roles, name="group sechs") is not None and random.random() < 0.001:
        await message.channel.send(f'shut up {message.author.mention}')

    if 'peepee' in message.content.lower():
        await message.channel.send("poopoo")

    if 'poopoo' in message.content.lower():
        await message.channel.send("peepee")

    await bot.process_commands(message)


bot.run(TOKEN)
