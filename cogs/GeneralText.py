import discord
from discord.ext import commands
import random

class GeneralText(commands.cog):
    """ General text commands, such as .hello, .sheesh, .pp"""
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def hello(self, ctx):
        await ctx.send("Hello, I am Chad")

    @commands.command()
    async def sheesh(self, ctx):
        x = "e" * random.randrange(2, 30)
        await ctx.send("sh" + x + "sh")

    @commands.command()
    async def pp(self, ctx):
        message_author = ctx.message.author.name
        x = "=" * random.randrange(2, 40)
        await ctx.send(message_author + "'s pp length:  8" + x + "D")


def setup(bot):
    bot.add_cog(GeneralText(bot))
