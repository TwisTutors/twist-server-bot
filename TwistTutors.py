import discord, asyncio, time, random
from discord import message
from discord import colour
from discord.ext import commands
import random
from TwistTutorsToken import token
import asyncio

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
    assist_embed.add_field(name="Ask for help", value="`;help `")
    await ctx.send(embed=assist_embed)


@client.command()
async def delete(ctx, amount = 5):
    purge_amount = amount + 1
    await ctx.channel.purge(limit=purge_amount)

@client.command()
async def help(ctx):
    await ctx.channel.send(f"What topic would you like help in,{ctx.author.mention}?")
    def check(m):
        return m.author == ctx.author
    helptopic = await client.wait_for('message', check=check)
    if helptopic.content.lower() == "math" or helptopic.content.lower() == "m":
        await ctx.send(f"{ctx.author.mention}, specifically what type of math do you need help with?")

        def check(s):
            return s.author == ctx.author

        specific_math = await client.wait_for('message', check=check)
        if specific_math.content.lower() == "geo" or specific_math.content.lower() == "geometry":
            channel = client.get_channel(815741183078694932)
            await channel.send(f"<@&815739473035919420> A student, {ctx.author.mention} needs help with their geometry work!")

        if specific_math.content.lower() == "algebra 1" or specific_math.content.lower() == "alg 1" or specific_math.content.lower() == "alg1" or specific_math.content.lower() == "algebra1":
            channel = client.get_channel(815741141504360450)
            await channel.send(f"<@&815739473035919420> A student, {ctx.author.mention} needs help with their algebra 1 work!")

        if specific_math.content.lower() == "basic math" or specific_math.content.lower() == "basic" or specific_math.content.lower() == "basicmath":
            channel = client.get_channel(815741088522174504)
            await channel.send(f"<@&815739473035919420> A student, {ctx.author.mention} needs help with their basic math work!")

        if specific_math.content.lower() == "pre-algebra" or specific_math.content.lower() == "prealg" or specific_math.content.lower() == "prealgebra":
            channel = client.get_channel(815741115076575253)
            await channel.send(f"<@&815739473035919420> A student, {ctx.author.mention} needs help with their pre-algebra work!")

        if specific_math.content.lower() == "precalculus" or specific_math.content.lower() == "precalc" or specific_math.content.lower() == "pre calc" or specific_math.content.lower() == "pre calculus":
            channel = client.get_channel(815741321867689995)
            await channel.send(f"<@&815739473035919420> A student, {ctx.author.mention} needs help with their pre-calculus work!")

        if specific_math.content.lower() == "alg2" or specific_math.content.lower() == "algebra2" or specific_math.content.lower() == "alg 2" or specific_math.content.lower() == "algebra 2":
            channel = client.get_channel(815741205547188234)
            await channel.send(f"<@&815739473035919420> A student, {ctx.author.mention} needs help with their algebra-2 work!")

        if specific_math.content.lower() == "linear alg" or specific_math.content.lower() == "linear algebra" or specific_math.content.lower() == "linearalgebra":
            channel = client.get_channel(815741485705592844)
            await channel.send(f"<@&815739473035919420> A student, {ctx.author.mention} needs help with their linear algebra work!")

        if specific_math.content.lower() == "stats" or specific_math.content.lower() == "statistics" or specific_math.content.lower() == "stat":
            channel = client.get_channel(816515786654089226)
            await channel.send(f"<@&815739473035919420> A student, {ctx.author.mention} needs help with their linear statistics work!")








    elif helptopic.content.lower() == "ela" or helptopic.content.lower() == "e":
        await ctx.send(f"<@&815785109473984513> A student, {ctx.author.mention} needs help with their ELA work!")
    elif helptopic.content.lower() == "science" or helptopic.content.lower() == "sci" or helptopic.content.lower() == "s":
        await ctx.send(f"<@&815786846629265429> A student, {ctx.author.mention} needs help with their math work!")




    elif helptopic.content.lower() == "language" or helptopic.content.lower() == "lang" or helptopic.content.lower() == "l":
        await ctx.send(f"{ctx.author.mention}, what language do you need help in?", delete_after=7.5)

        def check(m):
            return m.author == ctx.author

        language_wait_for = await client.wait_for('message', check=check)
        if language_wait_for.content.lower() == "chinese":
            channel = client.get_channel(815742065526702131)
            await channel.send(f"<@&828284238847279176> A student, {ctx.author.mention} needs help with chinese homework!")


        elif language_wait_for.content.lower() == "spanish":
            channel = client.get_channel(815742051370401803)
            await channel.send(f"<@&828285201645830205> A student, {ctx.author.mention} needs help with spanish homework!")

        elif language_wait_for.content.lower() == "french":
            channel = client.get_channel(815742120928608316)
            await channel.send(f"<@&828308062786945065> A student, {ctx.author.mention} needs help with french homework!")
        #finished up to french


    elif helptopic.content.lower() == "social studies" or helptopic.content.lower() == "ss" or helptopic.content.lower() == "history":
        await ctx.send(f"<@&819342428388589568> A student, {ctx.author.mention} needs help with their social studies homework!")

@client.command()
async def game(ctx, subject):
    if subject.lower() == "tictactoe":
        channel = ctx.channel
        def check(m):
            return m.channel == channel
        playing = True
        A1 = ":white_large_square:"
        A2 = ":white_large_square:"
        A3 = ":white_large_square:"
        B1 = ":white_large_square:"
        B2 = ":white_large_square:"
        B3 = ":white_large_square:"
        C1 = ":white_large_square:"
        C2 = ":white_large_square:"
        C3 = ":white_large_square:"
        AIPlay = ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3"]
        Move = 1
        int(Move)
        while(playing):
            Tic_Emb = discord.Embed(
                title="Tic Tac Toe",
                colour=discord.Colour.dark_purple(),
                description=None
            )
            Tic_Emb.add_field(name="Game:",value= A1 + "  |  " + A2 + "  |  " + A3 + "\n" + "+—-—--—-+" + "\n" + B1 + "  |  " + B2 + "  |  " + B3 + "\n" + "+—-—--—-+" + "\n" + C1 + "  |  " + C2 + "  |  " + C3, inline=False)
            await ctx.send(embed=Tic_Emb)
            await channel.send("Move")
            await channel.send(Move)
            time.sleep(2)
            Your_Move = await client.wait_for('message', check=check)
            time.sleep(2)
            print(AIPlay)
            if Your_Move.content == "A1" and A1 == ":white_large_square:":
                A1 = ":x:"
                AIPlay.remove("A1")
            elif Your_Move.content == "A2" and A2 == ":white_large_square:":
                A2 = ":x:"
                AIPlay.remove("A2")
            elif Your_Move.content == "A3" and A3 == ":white_large_square:":
                A3 = ":x:"
                AIPlay.remove("A3")
            elif Your_Move.content == "B1" and B1 == ":white_large_square:":
                B1 = ":x:"
                AIPlay.remove("B1")
            elif Your_Move.content == "B2" and B2 == ":white_large_square:":
                B2 = ":x:"
                AIPlay.remove("B2")
            elif Your_Move.content == "B3" and B3 == ":white_large_square:":
                B3 = ":x:"
                AIPlay.remove("B3")
            elif Your_Move.content == "C1" and C1 == ":white_large_square:":
                C1 = ":x:"
                AIPlay.remove("C1")
            elif Your_Move.content == "C2" and C2 == ":white_large_square:":
                C2 = ":x:"
                AIPlay.remove("C2")
            elif Your_Move.content == "C3" and C3 == ":white_large_square:":
                C3 = ":x:"
                AIPlay.remove("C3")
            elif Your_Move.content == "Quit":
                break
            else: 
                continue

            Move = Move + 1
            print(AIPlay)
            AIPlayedMove = random.choice(AIPlay)
            if AIPlayedMove == "A1" and A1 == ":white_large_square:":
                A1 = ":o:"
                AIPlay.remove("A1")
            elif AIPlayedMove == "A2" and A2 == ":white_large_square:":
                A2 = ":o:"
                AIPlay.remove("A2")
            elif AIPlayedMove == "A3" and A3 == ":white_large_square:":
                A3 = ":o:"
                AIPlay.remove("A3")
            elif AIPlayedMove == "B1" and B1 == ":white_large_square:":
                B1 = ":o:"
                AIPlay.remove("B1")
            elif AIPlayedMove == "B2" and B2 == ":white_large_square:":
                B2 = ":o:"
                AIPlay.remove("B2")
            elif AIPlayedMove == "B3" and B3 == ":white_large_square:":
                B3 = ":o:"
                AIPlay.remove("B3")
            elif AIPlayedMove == "C1" and C1 == ":white_large_square:":
                C1 = ":o:"
                AIPlay.remove("C1")
            elif AIPlayedMove == "C2" and C2 == ":white_large_square:":
                C2 = ":o:"
                AIPlay.remove("C2")
            elif AIPlayedMove == "C3" and C3 == ":white_large_square:":
                C3 = ":o:"
                AIPlay.remove("C3")








client.run(token)
