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
    bot.loop.create_task(status_task())

# Status
async def status_task():
    while True:
        await bot.change_presence(activity=discord.Game(name='B>log', type=2, url='https://github.com/JuanRTech/beanbot'))
        await asyncio.sleep(10)
        await bot.change_presence(activity=discord.Game(name='funny bot', type=1, url='https://github.com/JuanRTech/beanbot'))
        await asyncio.sleep(10)

# Join
class Join(commands.Cog):
    @bot.command(name='Join', description='Make the bot join your channel!', pass_context=True, aliases=['join'])
    async def join(ctx):
        try:
            channel = ctx.message.author.voice.channel
        except:
            # channel check
            await ctx.send('You ain\'t in a channel homie')
            return

        await ctx.send('It\'s gamer time')

        voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
        if voice and voice.is_connected():
            voice.stop()
            await voice.disconnect()

            voice = await channel.connect()
        else:
            voice = await channel.connect()
        
# Leave
class Leave(commands.Cog):
    @bot.command(name='Leave', description='Make the bot leave your channel!', pass_context=True, aliases=['leave'])
    async def leave(ctx):
        try:
            channel = ctx.message.author.voice.channel
        except:
            # channel check
            await ctx.send('You ain\'t in a channel homie')
            return

        await ctx.send('Yeet')

        voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
        voice.stop()
        await voice.disconnect()

# Logan Sounds
class LoganSounds(commands.Cog):
    @bot.command(name='LoganSounds', description='Play some epic logan sounds', pass_context=True, aliases=['log', 'logan', 'Logan'])
    async def playsound(ctx):
        try:
            channel = ctx.message.author.voice.channel
        except:
            # channel check
            await ctx.send('You ain\'t in a channel homie')
            return
        
        # channel info
        await ctx.send('Playing')
        voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
        if not voice or not voice.is_connected():
            voice = await channel.connect()
        
        source = discord.FFmpegPCMAudio('/home/bot-man/beanbot/sound/logan/' + random.choice(os.listdir('/home/bot-man/beanbot/sound/logan')))
        player = voice.play(source)

        # create stream
        while voice.is_playing():
            await asyncio.sleep(1)

# Clown
class Clown(commands.Cog):
    @bot.command(name='Clown', description='funny', pass_context=True, aliases=['clown', 'toot', 'trumpet'])
    async def playsound(ctx):
        try:
            channel = ctx.message.author.voice.channel
        except:
            # channel check
            await ctx.send('You ain\'t in a channel homie')
            return

        # channel info
        await ctx.send('Playing')
        voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
        if not voice or not voice.is_connected():
            voice = await channel.connect()

        source = discord.FFmpegPCMAudio('/home/bot-man/beanbot/sound/clown/' + random.choice(os.listdir('/home/bot-man/beanbot/sound/clown')))
        player = voice.play(source)

        # create stream
        while voice.is_playing():
            await asyncio.sleep(1)

#Poggers
class Poggers():
    async def playsound(message):
        try:
            channel = message.author.voice.channel
        except:
            # channel check
            return

        # channel info
        await message.channel.send('POGGERS')
        voice = discord.utils.get(bot.voice_clients, guild=message.guild)
        if not voice or not voice.is_connected():
            voice = await channel.connect()

        source = discord.FFmpegPCMAudio('/home/bot-man/beanbot/sound/poggers/' + random.choice(os.listdir('/home/bot-man/beanbot/sound/poggers')))
        player = voice.play(source)

        # create stream
        while voice.is_playing():
            await asyncio.sleep(1)

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

    if 'poggers' in message.content.lower():
        await Poggers.playsound(message)

    await bot.process_commands(message)


bot.run(TOKEN)
