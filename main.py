import search
import os
import discord
from discord.ext import commands

intents = discord.Intents.all()

bot = commands.Bot(command_prefix='.', help_command=None, intents=intents)

async def on_ready():
    await bot.change_presence(activity=discord.Game(name="hi"))
    print(f'We have logged in as {bot.user}')


def query(l, n, c, v, e):
    file_path = os.path.join("json", f"{l}_{n}.json")
    verses = search.load_verses_from_json(file_path)
    result = search.search_verses_in_json(verses, c, v, e)
    return result

#print(query("en", "kjv", "1", "1", "1"))

@bot.command(name="verse", help="Gives a bible verse.")
async def verse(ctx, *, text="nothing"):
  # Create an embed
  global message_count
  message_count += 1
  async with ctx.typing():
    result = ""
  # Send the embed as a message
  await ctx.send(result)

bot.run(os.environ.get("t"))