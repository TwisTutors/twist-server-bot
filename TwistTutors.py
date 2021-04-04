import discord, asyncio
from discord import message
from discord.ext import commands
import random
from TwistTutorsToken import token

client = commands.Bot(command_prefix= ";")

@client.event
async def on_ready():
    print("Twist Tutors is up and ready!")
    await client.change_presence(status=discord.Status.idle, activity=discord.Game('Watching over Twist Tutors!'))

@client.command()
async def web(ctx):
    website_embed = discord.Embed(
        title="__Come take a look at our server website!__",
        colour=discord.Colour.dark_purple(),
        description=None
    )
    website_embed.add_field(name="https://twisttutors.tk/",value="**" + "And as always, have fun learning and exploring!" + "**")
    website_embed.set_image(url="https://cdn.discordapp.com/attachments/819364098839805993/827520501030715392/twisttutors.png")
    await ctx.send(embed=website_embed)

@client.command()
async def website(ctx):
    website_embed = discord.Embed(
        title="__Come take a look at our server website!__",
        colour=discord.Colour.dark_purple(),
        description=None
    )
    website_embed.add_field(name="https://twisttutors.tk/",value="**" + "And as always, have fun learning and exploring!" + "**")
    website_embed.set_image(url="https://cdn.discordapp.com/attachments/819364098839805993/827520501030715392/twisttutors.png")
    await ctx.send(embed=website_embed)



@client.command()
async def clear(ctx, amount = 5):
    purge_amount = amount + 1
    await ctx.channel.purge(limit=purge_amount)






client.run(token)