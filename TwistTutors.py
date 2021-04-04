import discord, asyncio, time, random
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
    await client.change_presence(status=discord.Status.online, activity=discord.Game(';assist|At your service!'))

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
    assist_embed.add_field(name="Ask for math help", value="`;help math`")
    await ctx.send(embed=assist_embed)


@client.command()
async def clear(ctx, amount = 5):
    purge_amount = amount + 1
    await ctx.channel.purge(limit=purge_amount)

@client.command()
async def help(ctx, subject):
    if subject.lower() == "math" or subject.lower() == "m":
        await ctx.send(f"<@&815739473035919420> A student, {ctx.author.mention} needs help with their math homework!")
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
        AIPlay = ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3"]
        Move = 1
        int(Move)
        while(playing):
            Tic_Emb = discord.Embed(
                title="Tic Tac Toe",
                colour=discord.Colour.dark_purple(),
                description=None
            )
            Tic_Emb.add_field(name="Game:",value= A1 + "  |  " + A2 + "  |  " + A3 + "\n" + B1 + "  |  " + B2 + "  |  " + B3 + "\n" + C1 + "  |  " + C2 + "  |  " + C3, inline=False)
            await ctx.send(embed=Tic_Emb)
            await channel.send("Move")
            await channel.send(Move)
            time.sleep(2)
            Your_Move = await client.wait_for('message', check=check)
            time.sleep(2)
            print(AIPlay)
            if Your_Move.content == "A1" and A1 == ".":
                A1 = "X"
                AIPlay.remove("A1")
            if Your_Move.content == "A2" and A2 == ".":
                A2 = "X"
                AIPlay.remove("A2")
            if Your_Move.content == "A3" and A3 == ".":
                A3 = "X"
                AIPlay.remove("A3")
            if Your_Move.content == "B1" and B1 == ".":
                B1 = "X"
                AIPlay.remove("B1")
            if Your_Move.content == "B2" and B2 == ".":
                B2 = "X"
                AIPlay.remove("B2")
            if Your_Move.content == "B3" and B3 == ".":
                B3 = "X"
                AIPlay.remove("B3")
            if Your_Move.content == "C1" and C1 == ".":
                C1 = "X"
                AIPlay.remove("C1")
            if Your_Move.content == "C2" and C2 == ".":
                C2 = "X"
                AIPlay.remove("C2")
            if Your_Move.content == "C3" and C3 == ".":
                C3 = "X"
                AIPlay.remove("C3")
            if Your_Move.content == "Quit":
                break
            Move = Move + 1
            print(AIPlay)
            AIPlayedMove = random.choice(AIPlay)
            if AIPlayedMove == "A1" and A1 == ".":
                A1 = "O"
                AIPlay.remove("A1")
            if AIPlayedMove == "A2" and A2 == ".":
                A2 = "O"
                AIPlay.remove("A2")
            if AIPlayedMove == "A3" and A3 == ".":
                A3 = "O"
                AIPlay.remove("A3")
            if AIPlayedMove == "B1" and B1 == ".":
                B1 = "O"
                AIPlay.remove("B1")
            if AIPlayedMove == "B2" and B2 == ".":
                B2 = "O"
                AIPlay.remove("B2")
            if AIPlayedMove == "B3" and B3 == ".":
                B3 = "O"
                AIPlay.remove("B3")
            if AIPlayedMove == "C1" and C1 == ".":
                C1 = "O"
                AIPlay.remove("C1")
            if AIPlayedMove == "C2" and C2 == ".":
                C2 = "O"
                AIPlay.remove("C2")
            if AIPlayedMove == "C3" and C3 == ".":
                C3 = "O"
                AIPlay.remove("C3")








client.run(token)