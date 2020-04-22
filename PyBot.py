import discord
from discord.ext import commands
import os

#client = discord.Client()
client = commands.Bot(command_prefix = '!')
token = "Token"

directory = "H:\\PyBot\\"

@client.event
async def on_ready():
    print('Bot Online.')
    await client.change_presence(status=discord.Status.online, activity=discord.Game('Type !help to start'))

@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')


@client.command(pass_context=True)
async def ping(ctx):
    await ctx.send("Pong! Latency: " + str(round(client.latency * 1000)) + "ms.")

@client.command(pass_context=True)
async def clear(ctx, amount=5):
    await ctx.send("No permission to remove messages")
    #await ctx.channel.purge(limit = amount)


for filename in os.listdir('./cogs'):
    if(filename.endswith('.py')):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run(token)
