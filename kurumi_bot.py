import traceback
import os
import discord
from discord.ext import commands
from datetime import datetime
from ruamel.yaml import YAML

yaml = YAML(typ="safe")
yaml.indent(mapping=2, sequence=4, offset=2)

with open("discord.yaml") as f:
    config = yaml.load(f)

token = config["bot"]["token"]

cmd_prefix = config["bot"]["cmd_prefix"]
description = config["bot"]["description"]


class KurumiBot(commands.Bot):
    def __init__(self, **options):
        super().__init__(cmd_prefix, description=description, **options)
        #reddit = apraw.Reddit(client_id=CLIENT_ID, client_secret=CLIENT_SECRET,
        #              username=USERNAME, password=PASSWORD, user_agent=USER_AGENT)
        #Banhammer.__init__(self, reddit, bot=self)

    async def on_ready(self):
        print(f"{self.user.name} is running.")
        #await self.add_subreddits(SUBNAME)
        #Banhammer.start(self)

    async def on_command_error(self, ctx: commands.Context, error: Exception):
        if isinstance(error, discord.ext.commands.errors.CommandNotFound):
            pass
        else:
            await ctx.message.channel.send(error)
            traceback.print_tb(error.__traceback__)

    @property
    def embed(self):
        embed = discord.Embed(
            colour=discord.Colour(0).from_rgb(186, 179, 255)
        )
        embed.set_footer(text=f"KurumiBot", icon_url=self.user.avatar_url)
        embed.timestamp = datetime.utcnow()

        return embed

    #@EventHandler.new()
    #@EventHandler.comments()
    #async def handle_new(self, p: RedditItem):
    #    msg = await self.get_channel(CHANNEL_ID).send(embed=await p.get_embed(embed_template=self.embed))
    #    await p.add_reactions(msg)


cogs = config["cogs"]

if __name__ == "__main__":
    bot = KurumiBot(owner_id=321566831670198272)

    for cog in cogs:
        bot.load_extension(cog)
        print(f"Cog: {cog} loaded.")

    bot.run(token)

