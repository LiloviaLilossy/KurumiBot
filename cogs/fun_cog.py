from typing import TYPE_CHECKING
from random import choice

import discord
from discord.ext import commands

if TYPE_CHECKING:
    from kurumi_bot import KurumiBot

class FunCog(commands.Cog):
    def __init__(self, bot: 'KurumiBot'):
        bot.is_huggable = True
        bot.is_pattable = True
        self.bot = bot
        self.allowed = [276241808584081410, 154328221154803712, 176019364234002443]

    @commands.command()
    async def precure(self, ctx: commands.Context):
        """
        I'll give you a random Cure!
        """
        with open("lists/precure.txt", "r") as f:
            cures = f.readlines()
        await ctx.send(choice(cures))
    
    @commands.command()
    async def hug(self, ctx: commands.Context, people: commands.Greedy[discord.Member], *, reason: str = "I love them"):
        owner = ctx.guild.get_member(self.bot.owner_id)
        if owner in people and not ctx.bot.is_huggable:
            if ctx.author.id in self.allowed: pass
            elif len(people) > 1:
                people.remove(owner)
            else:
                return await ctx.send("Lilo said she's not huggable.")
        tohug = [member.mention for member in people]
        msg = ", ".join(tohug)
        await ctx.send(f"*hugs {msg} because {reason}*")
    
    @commands.command()
    async def pat(self, ctx: commands.Context, people: commands.Greedy[discord.Member], *, reason: str = "they deserve it"):
        owner = ctx.guild.get_member(self.bot.owner_id)
        if owner in people and not ctx.bot.is_pattable:
            if ctx.author.id in self.allowed: pass
            elif len(people) > 1:
                people.remove(owner)
            else:
                return await ctx.send("Lilo said she's not pattable.")
        tohug = [member.mention for member in people]
        msg = ", ".join(tohug)
        await ctx.send(f"*pat-pat {msg} because {reason}*")

def setup(bot: 'KurumiBot'):
    bot.add_cog(FunCog(bot))
