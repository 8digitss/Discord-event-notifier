import discord
from discord.ext import commands, tasks
from database import add_event, list_events, get_upcoming_events
import asyncio

TOKEN = "YOUR_DISCORD_BOT_TOKEN"

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}")
    event_reminder.start()

@bot.command()
async def addevent(ctx, title: str, time: str, *, description: str):
    add_event(title, time, description)
    await ctx.send(f"Event '{title}' added successfully!")

@bot.command()
async def listevents(ctx):
    events = list_events()
    if not events:
        await ctx.send("No upcoming events.")
    else:
        message = "**Upcoming Events:**\n"
        for event in events:
            message += f"**{event[1]}** at {event[2]} - {event[3]}\n"
        await ctx.send(message)

@tasks.loop(minutes=1)
async def event_reminder():
    events = get_upcoming_events()
    for event in events:
        channel = discord.utils.get(bot.get_all_channels(), name='general')
        if channel:
            await channel.send(f"Reminder: Event '{event[1]}' is starting soon!")

bot.run(TOKEN)
