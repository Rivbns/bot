import discord
from discord.components import Select, SelectOption, Button
from discord.ext import commands
import asyncio
from asyncio import run_coroutine_threadsafe
from urllib import parse, request
import re
import os
from youtube_dl import YoutubeDL

class music_cog(commands.Cog):
    def __init__ (self, bot):
        self.bot = bot
