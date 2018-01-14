import discord
import asyncio

bot = discord.Client()

empty = " ̷̧̟̭̺͕̜̦̔̏̊̍ͧ͊́̚̕͞"


@bot.event
@asyncio.coroutine
def on_ready():
    print("Logged in as",bot.user.name)
    print("Id:",bot.user.id)
    print("Bot ready.")


@bot.event
@asyncio.coroutine
def on_message(message):
    if message.author == bot.user:
        return
    elif message.content.startswith("The bot"):
        yield from bot.send_message(message.channel, "Stop talking about me")
    elif message.content.startswith("Dop"):
        yield from bot.send_message(message.channel, "He is amazing am I right!")
    elif message.content.startswith("!Clearance-Show-Embed"):
        embed = discord.Embed(title="Clearance Levels:", color=0x9cd616)
        embed.add_field(name=empty, value="Onyx - Black - X\nIvory - White - 4\nShamrock - Green - 3\nMarigold - Yello"
                                          "w - 2\nCobalt - Blue - 1", inline=False)
        embed.add_field(name="------------------------", value="Onyx is the Highest.\nCobalt is the Lowes"
                                                               "t", inline=False)
        yield from bot.send_message(message.channel, embed=embed)
        yield from bot.delete_message(message)
    elif message.content.startswith("!invite"):
        if "recruiter" in [y.name.lower() for y in message.author.roles]:
            invite = yield from bot.create_invite(message.channel, max_uses=1)
            embed = discord.Embed(title="Single Use Invite:", description=invite.url, color=0x9cd616)
            yield from bot.send_message(message.channel, embed=embed)
        else:
            embed = discord.Embed(title="Error:", description="You are not a recruiter! If this is an error please cont"
                                                              "act @cecilioacc#0219.")
            yield from bot.send_message(message.channel, embed=embed)
            return

bot.run("NDAxNTg2MDM4MjAxNTE2MDMy.DTsVsw.krSRHMWKOC4gA90eHOSAoIpvVX4")
