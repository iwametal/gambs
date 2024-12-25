import discord

from constants import channels, pokemon_data, rand_stats
from discord.ext import commands
from helper import Helper


### ENV VARIABLES ###
gen_data = Helper.get_general_env('.env')


def get_prefix(bot, message):
    prefixes = ['+']
    # You can add more complex logic here to determine the prefix
    return commands.when_mentioned_or(*prefixes)(bot, message)

intents = discord.Intents.default()
intents.members = True
intents.message_content = True
intents.messages = True


class ShroomBot(commands.Bot):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # POKEMON_DATA
        self.pokemon_data = pokemon_data
        self.rand_stats = rand_stats

        # GAMBLE CHANNELS
        self.channels = channels

        # self.EVENT_ROLL = {
        #     'event_active': False,
        #     'event_channels': event_channel_list,
        #     'roll_number': 0,
        #     'roll_max': 0
        # }


    # ON BOT START
    async def on_ready(self):
        print(f'Logged in as {self.user}')
        print('------')
        await self.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="Shrooms"))
        print("Shroom bot is up")


    # # SYNC SLASH COMMANDS WITH ?sync
    # from typing import Literal, Optional
    # @bot.command()
    # @commands.guild_only()
    # @commands.is_owner()
    # async def sync(ctx: commands.Context, guilds: commands.Greedy[discord.Object], spec: Optional[Literal["~", "*", "^"]] = None) -> None:
    #     if not guilds:
    #         if spec == "~":
    #             synced = await ctx.bot.tree.sync(guild=ctx.guild)
    #         elif spec == "*":
    #             ctx.bot.tree.copy_global_to(guild=ctx.guild)
    #             synced = await ctx.bot.tree.sync(guild=ctx.guild)
    #         elif spec == "^":
    #             ctx.bot.tree.clear_commands(guild=ctx.guild)
    #             await ctx.bot.tree.sync(guild=ctx.guild)
    #             synced = []
    #         else:
    #             synced = await ctx.bot.tree.sync()

    #         await ctx.send(
    #             f"Synced {len(synced)} commands {'globally' if spec is None else 'to the current guild.'}"
    #         )
    #         return

    #     ret = 0
    #     for guild in guilds:
    #         try:
    #             await ctx.bot.tree.sync(guild=guild)
    #         except discord.HTTPException:
    #             pass
    #         else:
    #             ret += 1

    #     await ctx.send(f"Synced the tree to {ret}/{len(guilds)}.")

    async def setup_hook(self):
        import glob
        import os

        cog_folders = ['gamble', 'generic']

        for folder in cog_folders:
            cog_files = glob.glob(os.path.join(f"cogs/{folder}", "*.py"))
            # cog_files = glob.glob(os.path.join("cogs", "*.py"))

            for cog_f in cog_files:
                if cog_f.endswith(".py") and not cog_f.endswith("__init__.py"):
                    cog = os.path.splitext(os.path.basename(cog_f))[0]
                    cog_path = f"cogs.{folder}.{cog}"
                    try:
                        await self.load_extension(cog_path)
                        print(f"Loaded {cog_path}")
                    except Exception as e:
                        print(f"Failed to load {cog_path}: {e}")


if __name__ == '__main__':
    bot = ShroomBot(command_prefix=get_prefix, intents=intents)

    bot.run(gen_data['BOT_TOKEN'])