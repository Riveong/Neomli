import discord
import os
import random
from discord.ext import commands
from dotenv import load_dotenv
from PIL import Image, ImageDraw


load_dotenv()
TOKEN = os.getenv('token')

intents = discord.Intents.default()  # Create a new Intents instance
intents.message_content = True

class ImageHelpCommand(commands.HelpCommand):
    async def send_bot_help(self, mapping):
        # Create an embed...

        file = discord.File("help.png", filename="help.png")

        # Send the embed...
        await self.get_destination().send(file=file)

bot = commands.Bot(command_prefix='!', help_command=ImageHelpCommand(),  intents=intents)

'''
Common Commands

'''
#hi
@bot.command(name='hi')
async def hi(ctx):
    await ctx.send('hello')

'''
Dice Commands

'''
#dice
@bot.command(name='dice')
async def dice(ctx):
    await ctx.send('')

#d20
@bot.command(name='dice20')
async def dice(ctx):
    await ctx.send(random.randint(1,20))
    
#d6
@bot.command(name='dice6')
async def dice(ctx):
    await ctx.send(random.randint(1,6))
    
#d8
@bot.command(name='dice8')
async def dice(ctx):
    await ctx.send(random.randint(1,8))
    
#d4
@bot.command(name='dice4')
async def dice(ctx):
    await ctx.send(random.randint(1,4))

bot.run(TOKEN)
