import discord
from discord.ext import commands

directory = "H:\\PyBot\\"

class People(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    @commands.Cog.listener()
    async def on_ready(self):
        print("People module is online.")

    @commands.command(aliases=['peter', 'pete', 'Peter', 'Pete'])
    async def _peter(self, ctx):
        await ctx.send("Please refer to him as: afro-asiatic ethno-racial-nationalist Petras Pareskeoudou")

    @commands.command(aliases=['afro-asiatic ethno-racial-nationalist Petras Pareskeoudou', 'Afro-Asiatic ethno-racial-nationalist Petras Pareskeoudou', 'afro-asiatic ethno-racial-nationalist petras pareskeoudou'])
    async def _AAERNPP(self, ctx):
        await ctx.send("Please refer to him as: Afro-Asiatic ethno-racial-nationalist Petras Pareskeoudou")

    @commands.command(aliases=['jacob', 'Jacob'])
    async def _jacob(self, ctx):
        await ctx.send("You mean gaycum?")

    @commands.command(aliases=['Chris', 'chris'])
    async def _chris(self, ctx):
        await ctx.send(file=discord.File(directory + 'unholy2.png'))

    @commands.command(aliases=['Victor', 'victor'])
    async def _victor(self, ctx):
        await ctx.send(file=discord.File(directory + 'victor.png'))

    @commands.command(aliases=['babyIboane', 'babyiboane'])
    async def _babyIboane(self, ctx):
        await ctx.send(file=discord.File(directory + 'babyIboane.png'))

def setup(client):
    client.add_cog(People(client))