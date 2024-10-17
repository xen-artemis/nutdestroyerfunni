"""
this is just for educational purposes !!!
"""

import discord
from discord.ext import commands
import asyncio
import aiohttp # prob wont use this but just in case
from itertools import cycle

with open("C:/Users/Administrator/Downloads/voidsec.png", "rb") as file: # replace this with your own file path
  servicon = file.read()

penny = "token here"

msgcum = ["@everyone yeah idk"]
# add , after " to add more messagess
channels = cycle(["nuked by nutdestroyer420", "gachas are scared", "property of nutdestroyer420"]) 
                                              # ^^ genuinely the cringest shit i had to ever type out but ehh
servname = "Romania" # real

rolename = channels

webhooknames = channels

voidsec = commands.Bot(command_prefix="v!", intents=discord.Intents.all())
