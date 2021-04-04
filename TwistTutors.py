import discord, asyncio, time
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
        await ctx.send(f"<@&815739473035919420> {ctx.author.mention} needs help with his math homework!")
    elif subject.lower() == "ela" or subject.lower() == "e":
        await ctx.send(f"<@&815785109473984513> {ctx.author.mention} needs help with his ELA homework!")
    elif subject.lower() == "science" or subject.lower() == "sci" or subject.lower() == "s":
        await ctx.send(f"<@&815786846629265429> {ctx.author.mention} needs help with his math homework!")
    elif subject.lower() == "language" or subject.lower() == "lang" or subject.lower() == "l":
        channel = ctx.channel
        await ctx.send(f"{ctx.author.mention}, what language do you need help in?")

        def check(m):
            return m.channel == channel

        language_wait_for = await client.wait_for('message', check=check)
        if language_wait_for.content == "chinese":
            await channel.send(f"@Chinese Tutor {ctx.author} needs help with chinese homework!")
        elif language_wait_for.content == "spanish":
            await channel.send(f"@Spanish Tutor {ctx.author} needs help with spanish homework!")
        else:
            await channel.send("Sorry that is not a language we support yet, but feel free to ask one of the staff members to add it!")
    elif subject.lower() == "social studies" or subject.lower() == "ss" or subject.lower() == "history":
        await ctx.send(f"<@&819342428388589568> {ctx.author.mention} needs help with his social studies homework!")

@client.command()
async def game(ctx, subject):
    if subject.lower() == "tictactoe":
        channel = ctx.channel
        def check(m):
            return m.channel == channel
        playing = True
        A1 = "."
        A2 = "."
        A3 = "."
        B1 = "."
        B2 = "."
        B3 = "."
        C1 = "."
        C2 = "."
        C3 = "."
        while(playing):
            await channel.send("Your Move")
            Your_Move = await client.wait_for('message', check=check)
            time.sleep(1)
            print(Your_Move)
            if Your_Move.content == "A1":
                A1 = "X"
                print(A1)








client.run(token)