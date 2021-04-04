import discord, asyncio
from discord import message
from discord import colour
from discord.ext import commands
import random
from TwistTutorsToken import token

client = commands.Bot(command_prefix= ";")

client.remove_command('help')

@client.event
async def on_ready():
    print("Twist Tutors is up and ready!")
    await client.change_presence(status=discord.Status.online, activity=discord.Game('At your service!'))

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
async def assist(ctx):
    assist_embed = discord.Embed(
        title=" 👋 Here are all the commands our bot has!",
        colour=discord.Colour.dark_gold(),
        description=None
    )
    assist_embed.add_field(name="Help", value="`;assist`", inline=True)
    assist_embed.add_field(name="View our website", value="`;web`", inline=True)
    assist_embed.add_field(name="Ask for  math help", value="`;math_help`")


    await ctx.send(embed=assist_embed)


@client.command()
async def clear(ctx, amount = 5):
    purge_amount = amount + 1
    await ctx.channel.purge(limit=purge_amount)

@client.command()
async def help(ctx, subject):
    if subject.lower() == "math" or subject.lower() == "m":
        await ctx.send(f"@Math Tutor {ctx.author} needs help with his math homework!")
    elif subject.lower() == "ela" or subject.lower() == "e":
        await ctx.send(f"@ELA Tutor {ctx.author} needs help with his ELA homework!")
    elif subject.lower() == "science" or subject.lower() == "sci" or subject.lower() == "s":
        await ctx.send(f"@Science Tutor {ctx.author} needs help with his math homework!")
    elif subject.lower() == "language" or subject.lower() == "lang" or subject.lower() == "l":
        channel = ctx.channel
        await ctx.send(f"{ctx.author.mention}, what language do you need help in?")

        def check(m):
            return m.channel == channel

        language_wait_for = await client.wait_for('message', check=check)
        if language_wait_for == "chinese":
            await channel.send(f"@Chinese Tutor {ctx.author} needs help with chinese homework!")
        elif language_wait_for == "spanish":
            await channel.send(f"@Spanish Tutor {ctx.author} needs help with spanish homework!")
        else:
            await channel.send("Sorry that is not a language we support yet, but feel free to ask one of the staff members to add it!")
    elif subject.lower() == "social studies" or subject.lower() == "ss" or subject.lower() == "history":
        await ctx.send(f"@History Tutor {ctx.author} needs help with his social studies homework!")










client.run(token)