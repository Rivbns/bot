from discord.components import ComponentsBot
from settings import settings
from music_cog import music_cog

bot = ComponentsBot(command_prefix="!")
bot.add_cog(music_cog(bot))

bot.run(settings["TOKEN"])
