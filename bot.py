import discord
import time
from botLogic import *

Dtoken = "MTI4NDY1NDY5NTU3ODczMDUyOA.GiGPno.zuZpNwsE6XlO88SHmwNKZ0Dd-qJGE9mLtMeeuo"
Dsecret = "qeCXmpROrDKGpa8t2DLhwZRg9BMmMHlX"

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Hemos iniciado sesión como {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send("Hi!")
    elif message.content.startswith('$bye'):
        await message.channel.send("See you soon!")
    elif message.content.startswith("$passgen"):
        await message.channel.send(gen_pass(random.randint(10, 20)))
    elif message.content.startswith("$emoji"):
        await message.channel.send(gen_emodji())
    elif message.content.startswith("$flipCoin"):
        await message.channel.send(f"The coin landed in {flip_coin()}")
    else:
        await message.channel.send(message.content)

@client.event
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')



client.run(Dtoken)