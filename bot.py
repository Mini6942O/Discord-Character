import os
import discord
from discord.ext import commands

# Load environment variables from Render
TOKEN = os.environ.get("DISCORD_TOKEN")
CLIENT_ID = os.environ.get("CLIENT_ID")

if not TOKEN or not CLIENT_ID:
    raise ValueError("Missing DISCORD_TOKEN or CLIENT_ID in environment variables.")

# Set up bot with default intents
intents = discord.Intents.default()
intents.message_content = True  # Needed for reading normal messages
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user} (ID: {bot.user.id})")
    print("------")

@bot.command()
async def ping(ctx):
    """Replies with 'Pong!' and the latency."""
    await ctx.send(f"Pong! 🏓 Latency: {round(bot.latency * 1000)}ms")

bot.run(TOKEN)
