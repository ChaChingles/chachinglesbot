import discord
from discord.ext import commands
from boto.s3.connection import S3Connection
# from dotenv import load_dotenv
import os

# load_dotenv('.env')
bot = discord.Client()
# bot = commands.Bot(command_prefix='$')

@bot.event
async def on_ready():
    # print(bot.guilds)
    print('We have logged in as {0.user}'.format(bot))

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    # if message.content.startswith('$hello'):
        # print(message.author.id)
    # if message.author.id == 690939370089480252:
    if message.channel.id == 956868861112762388:
        # await message.channel.send('Hello!')
        # send message to a different channel
        # print(message.content)
        # print(message.author.mention)
        # bot.guilds.cache.get(940558872949702716).channels.cache.get(940558872949702719).send(message.content)
        all_channels = [887404584153251880, 829863135354945606, 953964147291340820]
        for i in all_channels:
            # await bot.get_channel(i).send(f"<@690939370089480252>\n" + "> " +message.content)
            await bot.get_channel(i).send(message.author.mention + "\n" + message.content)
        # await bot.get_guild(940558872949702716).get_channel(940558872949702719).send(f"<@690939370089480252>\n" + message.content)
        # get all guild
        
bot.run(os.environ['TOKEN'])