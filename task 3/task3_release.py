import random
import discord
from discord.ext import commands
import asyncpraw
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
REDDIT_CLIENT_ID = os.getenv("REDDIT_CLIENT_ID")
REDDIT_CLIENT_SECRET = os.getenv("REDDIT_CLIENT_SECRET")
REDDIT_USER_AGENT = "memebot"

PREFIX = '!'
intents = discord.Intents.all()
bot = commands.Bot(command_prefix=PREFIX, intents=intents)

@bot.command()
async def meme(ctx):
    async with asyncpraw.Reddit(
        client_id=REDDIT_CLIENT_ID,
        client_secret=REDDIT_CLIENT_SECRET,
        user_agent=REDDIT_USER_AGENT
    ) as reddit:
        subreddit = await reddit.subreddit("memes")
        memes_submission = subreddit.hot(limit=100)

        memes_list = [submission async for submission in memes_submission if not submission.stickied]

    submission = random.choice(memes_list)
    await ctx.send(submission.url)


@bot.command()
async def hello(ctx):
    await ctx.reply("hello")

bot.run(TOKEN)
