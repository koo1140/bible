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
async def verse(ctx, language, version, chapter, verse_number, edition):
    async with ctx.typing():
        # Call the query function with provided arguments
        result = query(language, version, chapter, verse_number, edition)
        
    # Send the result as a message
    await ctx.send(result)

bot.run()