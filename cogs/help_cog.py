from typing import TYPE_CHECKING

import discord
from discord.ext import commands
from cmds.help_cmd import HelpCommand

if TYPE_CHECKING:
    from kurumi_bot import KurumiBot


class HelpCog(commands.Cog):
    def __init__(self, bot: "KurumiBot"):
        self.bot = bot
        self._original_help_command = bot.help_command
        bot.help_command = HelpCommand()
        bot.help_command.cog = self

    def cog_unload(self):
        self.bot.help_command = self._original_help_command


def setup(bot: "KurumiBot"):
    bot.add_cog(HelpCog(bot))
