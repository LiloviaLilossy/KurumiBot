from typing import TYPE_CHECKING

import discord
from discord.ext import commands

if TYPE_CHECKING:
    from kurumi_bot import KurumiBot

class FunCog(commands.Cog):
    def __init__(self, bot: 'KurumiBot'):
        self.bot = bot

    @commands.command()
    async def command(self, ctx: commands.Context):
        pass

def setup(bot: 'KurumiBot'):
    bot.add_cog(FunCog(bot))
