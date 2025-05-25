import discord
from discord.ext import commands
from discord import Interaction

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@bot.event
async def on_ready():
    await bot.tree.sync()
    print(f'{bot.user} has connected to Discord!')

@bot.tree.command(name="ping", description="Shows the ping!")
async def ping(interaction : Interaction):
    bot_latency = round(bot.latency)*1000
    await interaction.response.send_message(f'Ping : {bot_latency}ms')

@bot.command()
async def hello(ctx):
    await ctx.send("Hello!")

bot.run('YOUR_BOT_TOKEN')
