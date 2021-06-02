import discord, asyncio, time, random
from discord import message
from discord import colour
from discord.ext import commands
import random
import json
import os
from TwistTutorsToken import token




os.chdir(r"/home/pi/Desktop/twist-server-bot")

intents = discord.Intents.default()
intents.members = True

client = commands.Bot(command_prefix= ";", intents=intents)


client.remove_command('help')

@client.event
async def on_ready():
    print("Twist Tutors is up and ready!")
    while(1):

        a = client.get_guild(815737997923188778)
        await client.change_presence(status=discord.Status.online, activity=discord.Game(f"Watching over {a.member_count} bright students!"))
        await asyncio.sleep(5)
    

@client.event
async def on_member_join(member):
    channel = client.get_channel(815737999228796960)
    welcome_embed = discord.Embed(
        title=f"{member.mention} has landed in our server! Lets all give a warm welcome!",
        colour=discord.Colour.dark_purple(),
        description=None
    )
    welcome_embed.set_image(url="https://cdn.discordapp.com/attachments/830072392734736404/830091902992252948/Twist-v2-PixTeller.gif")
    await channel.send(embed=welcome_embed)



@client.command()
async def socials(ctx):
    socials_embed = discord.Embed(
        title="**Come take a look at our server socials!**",
        colour=discord.Colour.dark_purple(),
        description=None
    )
    socials_embed.add_field(name="__" + " 💻Our Website!" + "__",value="https://twisttutors.tk/")
    socials_embed.add_field(name="__" + "▶ Our YouTube Channel!" + "__",value="https://www.youtube.com/channel/UCKy8FNfU0eyuSHwVK8i_fdw",inline=False)
    socials_embed.add_field(name="__" + "🕊Our Twitter!" + "__",value="https://twitter.com/TwistTutors",inline=False)
    socials_embed.add_field(name="__" + "♪Our TikTok!" + "__",value="https://www.tiktok.com/@twist_tutors_official?lang=en",inline=False)
    socials_embed.add_field(name="__" + "📷Our Instagram!" + "__",value="https://www.instagram.com/twist_tutors/",inline=False)

    socials_embed.set_image(url="https://cdn.discordapp.com/attachments/830072392734736404/830091902992252948/Twist-v2-PixTeller.gif")
    await ctx.send(embed=socials_embed)

@client.command()
async def assist(ctx):
    assist_embed = discord.Embed(
        title=" 👋 Here are all the commands our bot has!",
        colour=discord.Colour.dark_gold(),
        description=None
    )
    assist_embed.add_field(name="Help", value="`;assist`", inline=True)
    assist_embed.add_field(name="View our socials", value="`;socials`", inline=True)
    assist_embed.add_field(name="Ask for help", value="`;help`")
    assist_embed.add_field(name="TicTacToe", value="`;game tictactoe`")
    assist_embed.add_field(name="See our Socials", value="`;socials`")


    await ctx.send(embed=assist_embed)


@client.command()
async def delete(ctx, amount = 5):
    purge_amount = amount + 1
    await ctx.channel.purge(limit=purge_amount)



@client.command()
async def help(ctx):
    await ctx.channel.send(f"What topic would you like help in, {ctx.author.mention}?\n```ARM\nMath```\n```YAML\nELA```\n```ELM\nSocial Studies```\n```ARM\nScience```\n```YAML\nLanguage```\n```ELM\nCoding```\n```ARM\nArt```")
    def check(m):
        return m.author == ctx.author
    helptopic = await client.wait_for('message', check=check)

    if helptopic.content.lower() == "coding" or helptopic.content.lower() == "code":
        await ctx.send(f"{ctx.author.mention}, what language do you need help with?\n```ARM\nPYTHON```\n```YAML\nJAVASCRIPT```\n```ELM\nJAVA```\n```ARM\nC```\n```YAML\nHTML```\n```ELM\nOTHER```")

        def check(code):
            return code.author == ctx.author

        specific_code = await client.wait_for('message', check=check)
        if specific_code.content.lower() == "python" or specific_code.content.lower() == "py":
            channel = client.get_channel(816492686076149771)
            await channel.send(f"<@&816485437454549033> A student, {ctx.author.mention} requires immediate **PYTHON** help!")

        elif specific_code.content.lower() == "js" or specific_code.content.lower() == "javascript":
            channel = client.get_channel(816492703708872705)
            await channel.send(f"<@&816485437454549033> A student {ctx.author.mention} requires immediate **JAVASCRIPT** help!")

        elif specific_code.content.lower() == "java":
            channel = client.get_channel(816492714253484042)
            await channel.send(f"<@&816485437454549033> A student {ctx.author.mention} requires immediate **JAVA** help!")

        elif specific_code.content.lower() == "c":
            channel = client.get_channel(816492724794425364)
            await channel.send(f"<@&816485437454549033> A student {ctx.author.mention} requires immediate **C** help!")

        elif specific_code.content.lower() == "html":
            channel = client.get_channel(816492749767180328)
            await channel.send(f"<@&816485437454549033> A student {ctx.author.mention} requires immediate **HTML** help!")

        elif specific_code.content.lower() == "other":
            channel = client.get_channel(828331966201856090)
            await channel.send(f"<@&816485437454549033> A student {ctx.author.mention} requires help in another language!")

        else:
            await ctx.send("I'm sorry I didn't quite catch that...Please run the ;help command again!")








    if helptopic.content.lower() == "math" or helptopic.content.lower() == "m":
        await ctx.send(f"{ctx.author.mention}, specifically what type of math do you need help with?\n```ARM\nBasic Math```\n```YAML\nPre-Algebra```\n```ELM\nAlgebra-1```\n```ARM\nGeometry```\n```YAML\nAlgebra-2```\n```ELM\nPre-Calc```\n```ARM\nCalculus```\n```ARM\nLinear-Algebra```\n```YAML\nStatistics```")

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
        await ctx.send(f"{ctx.author.mention}, what part of ELA do you need help with?\n```ARM\nWriting```\n```YAML\nReading```")

        def check(ela):
            return ela.author == ctx.author

        specific_ela = await client.wait_for('message', check=check)

        if specific_ela.content.lower() == "writing" or specific_ela.content.lower() == "write":
            channel = client.get_channel(815741586549112862)
            await channel.send(f"<@&815785109473984513>! {ctx.author.mention} needs help with writing work!")

        if specific_ela.content.lower() == "reading" or specific_ela.content.lower() == "comp":
            channel = client.get_channel(815741609378316289)
            await channel.send(f"<@&815785109473984513>! {ctx.author.mention} needs help with reading work!")






    elif helptopic.content.lower() == "language" or helptopic.content.lower() == "lang" or helptopic.content.lower() == "l":
        await ctx.send(f"{ctx.author.mention}, what language do you need help in?\n```ARM\nCHINESE```\n```YAML\nSPANISH```\n```ELM\nFRENCH```\n```ARM\nLATIN```\n```YAML\nJAPANESE```\n```ELM\nKOREAN```\n```ARM\nRUSSIAN```\n```YAML\nOTHER```", delete_after=7.5)

        def check(m):
            return m.author == ctx.author

        language_wait_for = await client.wait_for('message', check=check)
        if language_wait_for.content.lower() == "chinese":
            channel = client.get_channel(815742065526702131)
            await channel.send(f"<@&828284238847279176> A student, {ctx.author.mention} needs help with **CHINESE** homework!")


        elif language_wait_for.content.lower() == "spanish" or language_wait_for.content.lower() == "espanol":
            channel = client.get_channel(815742051370401803)
            await channel.send(f"<@&828285201645830205> A student, {ctx.author.mention} needs help with **SPANISh** homework!")

        elif language_wait_for.content.lower() == "french":
            channel = client.get_channel(815742120928608316)
            await channel.send(f"<@&828308062786945065> A student, {ctx.author.mention} needs help with **FRENCH** homework!")

        elif language_wait_for.content.lower() == "latin":
            channel = client.get_channel(815742145716813824)
            await channel.send(f"<@&831598641322917919> A student, {ctx.author.mention} needs help with **LATIN** homework!")

        elif language_wait_for.content.lower() == "japanese" or language_wait_for.content.lower() == "japan":
            channel = client.get_channel(815742168852725760)
            await channel.send(f"<@&831599128906956850> A student, {ctx.author.mention} needs help with **JAPANESE** homework!")

        elif language_wait_for.content.lower() == "korean":
            channel = client.get_channel(815742185491923024)
            await channel.send(f"<@&831599823752527883> A student, {ctx.author.mention} needs help with **KOREAN** homework!")

        elif language_wait_for.content.lower() == "russian":
            channel = client.get_channel(831600158570446848)
            await channel.send(f"<@&831600382933336155> A student, {ctx.author.mention} needs help with **RUSSIAN** homework!")

        elif language_wait_for.content.lower() == "other":
            channel = ctx.channel
            no_lang_embed = discord.Embed(
                title="We apologize for this inconvenience we have caused. If you could please tell me what language you desire, we will be sure to make a role and channel for it ASAP!",
                colour=discord.Colour.random(),
                description=None
            )
            await channel.send(embed=no_lang_embed)

            def check(hello):
                return hello.author == ctx.author

            other_lang_response = await client.wait_for('message', check=check)
            other_lang_embed = discord.Embed(
                title=f"__{ctx.author}'s language request__",
                colour=discord.Colour.red(),
                description=other_lang_response.content
            )
            await ctx.send("Your requested language has been submitted to staff members. For now, sit tight and we will try to respond ASAP!")
            dan_id = client.get_user(638343481596706827)
            await dan_id.send(embed=other_lang_embed)
            eric_id = client.get_user(709788125278502912)
            await eric_id.send(embed=other_lang_embed)
            sam_id = client.get_user(472500911936372758)
            await sam_id.send(embed=other_lang_embed)













    elif helptopic.content.lower() == "social studies" or helptopic.content.lower() == "ss" or helptopic.content.lower() == "social":
        await ctx.send(f"{ctx.author.mention}, what type of social studies do you need help with?\n```ARM\nHistory```\n```YAML\nGovernment```\n```ELM\nGeography```")

        def check(ss):
            return ss.author == ctx.author

        specific_ss = await client.wait_for('message', check=check)

        if specific_ss.content.lower() == "history":
            channel = client.get_channel(815740451151413248)
            await channel.send(f"<@&819342428388589568>! {ctx.author.mention} needs help with **HISTORY** homework!")

        elif specific_ss.content.lower() == "gov" or specific_ss.content.lower() == "government":
            channel = client.get_channel(815740640646266882)
            await channel.send(f"<@&819342428388589568>! {ctx.author.mention} needs help with **GOVERNMENT** homework!")

        elif specific_ss.content.lower() == "geography":
            channel = client.get_channel(815740717258244197)
            await channel.send(f"<@&819342428388589568>! {ctx.author.mention} needs help with **GEOGRAPHY** homework!")

        else:
            await ctx.send(f"{ctx.author.mention} I do not quite comprehend. Please do\n```\n;help\n```\n and try again!")


    elif helptopic.content.lower() == "science" or helptopic.content.lower() == "sci":
        await ctx.send(f"{ctx.author.mention}, specifically what type of science do you need help with?\n```ELM\nEarth Science```\n```YAML\nGeology```\n```ELM\nLiving Environment```\n```ARM\nChemistry```\n```YAML\nBiology```\n```ELM\nPhysics```")

        def check(p):
            return p.author == ctx.author

        specific_sci = await client.wait_for('message', check=check)

        if specific_sci.content.lower() == "earthsci" or specific_sci.content.lower() == "earth-sci" or specific_sci.content.lower() == "earth science":
            channel = client.get_channel(815741782120726609)
            await channel.send(f"<@&815786846629265429> A student, {ctx.author.mention} needs help with **Earth Science**!")

        elif specific_sci.content.lower() == "geology":
            channel = client.get_channel(815741809727766539)
            await channel.send(f"<@&815786846629265429> A student, {ctx.author.mention} needs help with **Geology**!")

        elif specific_sci.content.lower() == "living environment" or specific_sci.content.lower() == "living" or specific_sci.content.lower() == "environment" or specific_sci.content.lower() == "livingenvir":
            channel = client.get_channel(815741834781261836)
            await channel.send(f"<@&815786846629265429> A student, {ctx.author.mention} needs help with **Living Environment**!")

        elif specific_sci.content.lower() == "chemistry" or specific_sci.content.lower() == "chem":
            channel = client.get_channel(815741858813706300)
            await channel.send(f"<@&815786846629265429> A student, {ctx.author.mention} needs help with **Chemistry**!")

        elif specific_sci.content.lower() == "bio" or specific_sci.content.lower() == "biology":
            channel = client.get_channel(815741873276190720)
            await channel.send(f"<@&815786846629265429> A student, {ctx.author.mention} needs help with **Biology**!")

        elif specific_sci.content.lower() == "physics" or specific_sci.content.lower() == "phy":
            channel = client.get_channel(815741887565922304)
            await channel.send(f"<@&815786846629265429> A student, {ctx.author.mention} needs help with **Physics**!")





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
            try:
                Tic_Emb = discord.Embed(
                    title="Tic Tac Toe",
                    colour=discord.Colour.dark_purple(),
                    description="Type Quit to quit"
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
                    await channel.send(f"😭 Sadly, {ctx.author.mention} thinks that I'm some sort of robot who doesn't care about the game. JK, but you have sucessfully quit the game.")
                    break
                else: 
                    continue

                if A1 == ":x:" and A2 == ":x:" and A3 == ":x:" or B1 == ":x:" and B2 == ":x:" and B3 == ":x:" or C1 == ":x:" and C2 == ":x:" and C3 == ":x:" or A1 == ":x:" and B1 == ":x:" and C1 == ":x:" or A2 == ":x:" and B2 == ":x:" and C2 == ":x:" or A3 == ":x:" and B3 == ":x:" and C3 == ":x:" or A1 == ":x:" and B2 == ":x:" and C3 == ":x:" or A3 == ":x:" and B2 == ":x:" and C1 == ":x:" :
                    await channel.send("Ayyyy you won 🎉!!")
                    break

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

                if A1 == ":o:" and A2 == ":o:" and A3 == ":o:" or B1 == ":o:" and B2 == ":o:" and B3 == ":o:" or C1 == ":o:" and C2 == ":o:" and C3 == ":o:" or A1 == ":o:" and B1 == ":o:" and C1 == ":o:" or A2 == ":o:" and B2 == ":o:" and C2 == ":o:" or A3 == ":o:" and B3 == ":o:" and C3 == ":o:" or A1 == ":o:" and B2 == ":o:" and C3 == ":o:" or A3 == ":o:" and B2 == ":o:" and C1 == ":o:" :
                    await channel.send("You Lost")
                    break

            except:
                await channel.send("It was a tie")
                break

@client.command()
async def stats(ctx, member : discord.Member = None):
    member = member or ctx.author

    await open_profile(member)

    users = await get_player_data()

    thanks_amt = users[str(member.id)]["Thanks"]

    stats_embed = discord.Embed(
        title=f"**{member}'s stats**",
        colour=discord.Colour.dark_gold(),
        description=None
    )
    stats_embed.add_field(name="__Thanks__", value=thanks_amt)
    await ctx.send(embed=stats_embed)

async def open_profile(member):

    users = await get_player_data()

    if str(member.id) in users:
        return False
    else:
        users[str(member.id)] = {}
        users[str(member.id)]["Thanks"] = 0

    with open("thankdata.json", "w") as f:
        json.dump(users, f)
    return True

async def get_player_data():
    with open("thankdata.json", "r") as f:
        users = json.load(f)
    return users


@client.command()
async def thank(ctx, member:discord.Member):
    member = member

    await open_profile(member)

    users = await get_player_data()

    if ctx.author != member:
        reason_for_thanks = discord.Embed(
            title=f"How did {member} help you?",
            colour=discord.Colour.teal(),
            description=None
        )
        await ctx.send(embed=reason_for_thanks)

        def check(y):
            return y.author == ctx.author



        reason_for_thanks_response = await client.wait_for('message', check=check)

        if reason_for_thanks_response != "":


            response = discord.Embed(
                title="Your gratitude has been noted!",
                colour=discord.Colour.dark_blue(),
                description=None
            )

            await ctx.send(embed=response)
            users[str(member.id)]["Thanks"] += 1
    else:
        no_thank_self = discord.Embed(
            title="YOU CAN'T THANK YOURSELF!!",
            colour=discord.Colour.dark_orange(),
            description=None
        )
        await ctx.send(embed=no_thank_self)



    with open("thankdata.json", "w") as f:
        json.dump(users, f)
    return True

@client.command()
async def search(ctx, *, args):
    list_of_lessons = {
        "surface area" : "https://youtube.com/playlist?list=PLwn_zWLzIz3Jq0Lj_QF772S853vGns2SN"
    }
    if args.content.lower() in list_of_lessons:
        lesson_embed = discord.Embed(
            title = "Here is a lesson/playlist related to your request!",
            colour = discord.Colour.orange()
        )
        lesson_embed.add_field(url=list_of_lessons[args.content.lower()])
        await ctx.send(embed=lesson_embed)

                          







client.run(token)
