import os
import random
import discord
import webbrowser
from discord.ext import commands

client = discord.Client()
bot = commands.Bot(command_prefix='$')

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

@bot.command(name="owner")
async def owner(ctx):
    owner = [ "My owner: Myster" 
    ]

    response = random.choice(owner)
    await ctx.send(response)

@bot.command(name="key")
async def search(ctx, search: str):
    look_up_term = (search)

    url = "https://www.g2a.com/search?query={}".format(look_up_term)

    response = (url)
    await ctx.send(response)

#@bot.command(name="join")
#async def join(ctx):
 #   channel = ctx.author.voice.channel
  #  vc = await channel.connect()

@bot.command(name="join")
async def join(ctx):
  name = print(ctx)
  if name.content == "join":
    channel = name.author.voice.channel
    vc = await channel.connect()

  elif name.content == "leave":
    for vc in client.voice_clients:
      if vc.guild == name.guild:
        await vc.disconnect()

#@bot.command(name="leave")
#async def leave(ctx):
 # if vc.guild == message.guild:
  #  await vc.disconnect()

#@bot.command(name="join")
#async def on_ready(ctx):
    #print('Logged in as')
    #print(client.user.name)
    #print(client.user.id)
    #print('------')

    #channel = client.get_channel('id')
    #await ctx.client.join_voice_channel(channel)
    #print('Bot joined the channel.')

bot.run("ODA5ODc4NzgyNzc2MTgwNzQ2.YCbgZA.lPtmoeDFJ2qVgC7RSo4oS3GT8IY")