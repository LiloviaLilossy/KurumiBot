from typing import TYPE_CHECKING

import discord
from discord.ext import commands

if TYPE_CHECKING:
    from kurumi_bot import KurumiBot

class AdminCog(commands.Cog):
    def __init__(self, bot: 'KurumiBot'):
        self.bot = bot
    
    async def cog_check(self, ctx):
        if ctx.author.id == self.bot.owner_id:
            return True
        return False

    @commands.command(aliases=["e"])
    async def echo(self, ctx: commands.Context, channel: discord.TextChannel = None, *, message):
        if not channel:
            channel = ctx.channel
        await channel.send(message)
    
    @commands.command()
    async def addcure(self, ctx: commands.Context, *, cure):
        with open("lists/precure.txt", "a") as f:
            f.write("\n")
            f.write(cure)
        await ctx.send("Done!")

def setup(bot: 'KurumiBot'):
    bot.add_cog(AdminCog(bot))
