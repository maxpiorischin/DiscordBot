import discord
from discord.ext import commands
import random, sys
sys.path.append("..")
from modules import Games

class OtherCommands(commands.Cog):
    """General commands that respond with a message"""
    def __init__(self, client):
        self.client = client

    #commands
    @commands.command(aliases = ['hi'])
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

    @commands.command()
    @commands.has_permissions(embed_links=True) #funny gif
    async def fart(self, ctx):
        await ctx.send("https://tenor.com/view/among-us-fart-poop-shit-fart-gif-18914562")

    @commands.command(aliases = ['8ball', 'question'])
    @commands.has_permissions(embed_links=True)  # funny gif
    async def _8ball(self, ctx, *search):
        msg = ' '.join(search)
        response = Games.response(msg)
        await ctx.send(response)
        print(response)

    @commands.command()
    @commands.has_permissions(embed_links=True)
    async def vibecat(self, ctx):
        await ctx.send("https://cdn.discordapp.com/emojis/817502837453619231.gif?v=1")

    @commands.command()
    @commands.has_permissions(embed_links=True)
    async def ridecat(self, ctx):
        await ctx.send("https://cdn.discordapp.com/emojis/833214796534251521.gif?v=1")

    @commands.command()
    @commands.has_permissions(embed_links=True)
    async def trumpetcat(self, ctx):
        await ctx.send("https://cdn.discordapp.com/emojis/833209656947113984.gif?v=1")

    @commands.command()
    @commands.has_permissions(embed_links=True)
    async def rainbowroach(self, ctx):
        await ctx.send("https://cdn.discordapp.com/emojis/833211453346807858.gif?v=1")

    @commands.command()
    @commands.has_permissions(embed_links=True)
    async def sedan(self, ctx):
        await ctx.send("https://tenor.com/view/suicide-sedan-oh-no-car-hearse-gif-16536143")

    @commands.command()
    @commands.has_permissions(embed_links=True)
    async def fubuki(self, ctx):
        await ctx.send("https://tenor.com/view/fubuki-hellish-blizzard-one-punch-man-gif-19744192")

    @commands.command()
    @commands.has_permissions(embed_links=True)
    async def baka(self, ctx):
        await ctx.send("https://tenor.com/view/baka-mangobaka-bakamango-mangobae-emfrizzle-gif-20783222")

    @commands.command()
    @commands.has_permissions(embed_links=True)
    async def sedan(self, ctx):
        await ctx.send("https://tenor.com/view/suicide-sedan-oh-no-car-hearse-gif-16536143")
        await ctx.send("dababy moment")

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def purge(self, ctx, amount=5):
        try:
            await ctx.channel.purge(limit=amount + 1)
        except:
            await ctx.send("Bot permission not granted!")




def setup(client):
    client.add_cog(OtherCommands(client))
