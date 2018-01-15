import discord
import asyncio
import time

bot = discord.Client()

ranks = {}
ranks['Onyx - X'] = {}
ranks['Ivory - 4'] = {}
ranks['Shamrock - 3'] = {}
ranks['Marigold - 2'] = {}
ranks['Cobalt - 1'] = {}

ranks['Onyx - X']["Doppler"] = ''

ranks['Ivory - 4']["cecilioacc"] = ''

ranks['Shamrock - 3']["razorsharp"] = ''

ranks['Marigold - 2']["krikesof"] = ''

ranks['Cobalt - 1']["Denialz"] = ''
ranks['Cobalt - 1']["GenX"] = ''
ranks['Cobalt - 1']["Potato"] = ''

empty = " ̷̧̟̭̺͕̜̦̔̏̊̍ͧ͊́̚̕͞"


@bot.event
@asyncio.coroutine
def on_ready():
    print("Logged in as", bot.user.name)
    print("Id:", bot.user.id)
    print("Bot ready.")


@bot.event
@asyncio.coroutine
def on_message(message):
    if message.author == bot.user:
        return
    elif message.content.startswith("The bot"):
        yield from bot.send_message(message.channel, "Stop talking about me")
        return
    elif message.content.startswith("Dop"):
        yield from bot.send_message(message.channel, "He is amazing am I right!")
        return
    elif message.content.startswith("!Clearance-Show-Embed"):
        embed = discord.Embed(title="Clearance Levels:", color=0x9cd616)
        embed.add_field(name=empty, value="Onyx - Black - X\nIvory - White - 4\nShamrock - Green - 3\nMarigold - Yellow"
                                          " - 2\nCobalt - Blue - 1", inline=False)
        embed.add_field(name="------------------------", value="Onyx is the Highest.\nCobalt is the Lowes"
                                                               "t", inline=False)
        yield from bot.send_message(message.channel, embed=embed)
        yield from bot.delete_message(message)
        return
    elif message.content.startswith("!invite"):
        if "recruiter" in [r.name.lower() for r in message.author.roles]:
            invite = yield from bot.create_invite(message.channel, max_uses=1)
            embed = discord.Embed(title="Single Use Invite:", description=invite.url, color=0x9cd616)
            yield from bot.send_message(message.channel, embed=embed)
            return
        else:
            embed = discord.Embed(title="Error:", description="You are not a recruiter! If this is an error please cont"
                                                              "act @cecilioacc#0219.")
            yield from bot.send_message(message.channel, embed=embed)
            return
    elif message.content.startswith("!fire"):
        command, target = str(message.content).split(" ", 3)
        yield from bot.send_message(message.channel, "You're fired "+target+"!")
        time.sleep(2)
        yield from bot.send_message(message.channel, "You're rehired "+target+"!")
        return
    elif message.content.startswith("!test"):
        yield from bot.send_message(message.channel, message.author.mention)
        print(message.author.mention)
        print(message.author.name)
        yield from bot.send_message(message.channel, "To Be Worked On")
        return
    elif message.content.startswith("!lord"):
        yield from bot.send_message(message.channel, "https://rosecitycomiccon.com/wp-content/uploads/2017/08/petercapa"
                                                     "ldi_600x600_acf_cropped.jpg")
        return
    elif message.content.startswith("!list"):
        args = str(message.content).split(" ")
        print(args[0])
        o, ivor, s, m, c = 1, 1, 1, 1, 1
        try:
            if args[1].lower() == "onyx":
                o, ivor, s, m, c = 1, 0, 0, 0, 0
            elif args[1].lower() == "ivory":
                o, ivor, s, m, c = 0, 1, 0, 0, 0
            elif args[1].lower() == "shamrock":
                o, ivor, s, m, c = 0, 0, 1, 0, 0
            elif args[1].lower() == "marigold":
                o, ivor, s, m, c = 0, 0, 0, 1, 0
            elif args[1].lower() == "cobalt":
                o, ivor, s, m, c = 0, 0, 0, 0, 1
            else:
                yield from bot.send_message(message.channel, "Invalid Argument. Proper Usage: !list {rank} {go_above}")
                return
            print(args[1])
        except IndexError:
            print("No Selection")
        try:
            if args[2].lower() == "+":
                if ivor == 1:
                    o = 1
                elif s == 1:
                    ivor, o = 1, 1
                elif m == 1:
                    s, ivor, o = 1, 1, 1
                elif c == 1:
                    m, s, ivor, o = 1, 1, 1, 1
            elif args[2].lower() == "-":
                if o == 1:
                    ivor, s, m, c = 1, 1, 1, 1
                elif ivor == 1:
                    s, m, c = 1, 1, 1
                elif s == 1:
                    m, c = 1, 1
                elif m == 1:
                    c = 1
            print(args[2])
        except IndexError:
            print("No +")
        if "employee of the month" in [r.name.lower() for r in message.author.roles]:
            onyx, ivo, sham, mar, cob = "Empty", "Empty", "Empty", "Empty", "Empty"
            for i in ranks['Onyx - X']:
                if onyx == "Empty":
                    onyx = ""
                onyx += i
                onyx += ", "
            for i in ranks['Ivory - 4']:
                if ivo == "Empty":
                    ivo = ""
                ivo += i
                ivo += ", "
            for i in ranks['Shamrock - 3']:
                if sham == "Empty":
                    sham = ""
                sham += i
                sham += ", "
            for i in ranks['Marigold - 2']:
                if mar == "Empty":
                    mar = ""
                mar += i
                mar += ", "
            for i in ranks['Cobalt - 1']:
                if cob == "Empty":
                    cob = ""
                cob += i
                cob += ", "
            embed = discord.Embed(title="Employees and Ranks:")
            if o == 1:
                embed.add_field(name="Onyx - X:", value=onyx, inline=False)
            if ivor == 1:
                embed.add_field(name="Ivory - 4:", value=ivo, inline=False)
            if s == 1:
                embed.add_field(name="Shamrock - 3:", value=sham, inline=False)
            if m == 1:
                embed.add_field(name="Marigold - 2:", value=mar, inline=False)
            if c == 1:
                embed.add_field(name="Cobalt - 1:", value=cob, inline=False)
            yield from bot.send_message(message.channel, embed=embed)
            return
        elif "administrator" in [r.name.lower() for r in message.author.roles]:
            onyx, ivo, sham, mar, cob = "Empty", "Empty", "Empty", "Empty", "Empty"
            for i in ranks['Onyx - X']:
                if onyx == "Empty":
                    onyx = ""
                onyx += i
                onyx += ", "
            for i in ranks['Ivory - 4']:
                if ivo == "Empty":
                    ivo = ""
                ivo += i
                ivo += ", "
            for i in ranks['Shamrock - 3']:
                if sham == "Empty":
                    sham = ""
                sham += i
                sham += ", "
            for i in ranks['Marigold - 2']:
                if mar == "Empty":
                    mar = ""
                mar += i
                mar += ", "
            for i in ranks['Cobalt - 1']:
                if cob == "Empty":
                    cob = ""
                cob += i
                cob += ", "
            embed = discord.Embed(title="Employees and Ranks:")
            if o == 1:
                embed.add_field(name="Onyx - X:", value=onyx, inline=False)
            if ivor == 1:
                embed.add_field(name="Ivory - 4:", value=ivo, inline=False)
            if s == 1:
                embed.add_field(name="Shamrock - 3:", value=sham, inline=False)
            if m == 1:
                embed.add_field(name="Marigold - 2:", value=mar, inline=False)
            if c == 1:
                embed.add_field(name="Cobalt - 1:", value=cob, inline=False)
            yield from bot.send_message(message.channel, embed=embed)
            return
        elif "head of security" in [r.name.lower() for r in message.author.roles]:
            onyx, ivo, sham, mar, cob = "Empty", "Empty", "Empty", "Empty", "Empty"
            for i in ranks['Onyx - X']:
                if onyx == "Empty":
                    onyx = ""
                onyx += i
                onyx += ", "
            for i in ranks['Ivory - 4']:
                if ivo == "Empty":
                    ivo = ""
                ivo += i
                ivo += ", "
            for i in ranks['Shamrock - 3']:
                if sham == "Empty":
                    sham = ""
                sham += i
                sham += ", "
            for i in ranks['Marigold - 2']:
                if mar == "Empty":
                    mar = ""
                mar += i
                mar += ", "
            for i in ranks['Cobalt - 1']:
                if cob == "Empty":
                    cob = ""
                cob += i
                cob += ", "
            embed = discord.Embed(title="Employees and Ranks:")
            if o == 1:
                embed.add_field(name="Onyx - X:", value=onyx, inline=False)
            if ivor == 1:
                embed.add_field(name="Ivory - 4:", value=ivo, inline=False)
            if s == 1:
                embed.add_field(name="Shamrock - 3:", value=sham, inline=False)
            if m == 1:
                embed.add_field(name="Marigold - 2:", value=mar, inline=False)
            if c == 1:
                embed.add_field(name="Cobalt - 1:", value=cob, inline=False)
            yield from bot.send_message(message.channel, embed=embed)
            return
        return
    elif message.content.startswith("!add"):
        args = str(message.content).split(" ")
        try:
            print(args[1])
        except IndexError:
            yield from bot.send_message(message.channel, "Invalid Argument. Proper Usage: !add {player} {rank}. {player"
                                                         "} cannot be a mention, just the actual name, not nickname. Ca"
                                                         "se Sensitive.")
            return
        try:
            print(args[2])
        except IndexError:
            yield from bot.send_message(message.channel, "Invalid Argument. Proper Usage: !add {player} {rank}. {player"
                                                         "} cannot be a mention, just the actual name, not nickname. Ca"
                                                         "se Sensitive.")
            return
        index = ''
        if str(args[2]).lower() == "ivory":
            index = 'Ivory - 4'
        elif str(args[2]).lower() == 'shamrock':
            index = 'Shamrock - 3'
        elif str(args[2]).lower() == 'marigold':
            index = 'Marigold - 2'
        elif str(args[2]).lower() == 'cobalt':
            index = 'Cobalt - 1'
        ranks[index][args[1]] = ''
    elif message.content.startswith("!"):
        yield from bot.send_message(message.channel, "Invalid Command.")
        return

bot.run("")
