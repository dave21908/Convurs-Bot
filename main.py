import discord
from discord.ext import commands
from mlogic import *
from model import get_class

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am {bot.user}. Nice to meet you!')

@bot.command()
async def wow(ctx, count_wow = 5):
    await ctx.send("wow" * count_wow)

@bot.command()
async def randomquote(ctx):
    await ctx.send(quoterandom())

@bot.command()
async def check(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            file_name = attachment.filename
            file_url = attachment.url
            await attachment.save(f"./{attachment.filename}")
            await ctx.send(f"Saving the images to ./{attachment.filename}")
            await ctx.send(get_class(model_path="./converted_keras3/keras_model.h5", labels_path="./converted_keras3/labels.txt", image_path=f"./{attachment.filename}"))
    else:
        await ctx.send("Where's your image? ¯\_(ツ)_/¯")

bot.run("[BOT TOKEN]")