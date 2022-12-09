import discord
import openai
from discord.ext import commands

# create a bot instance
bot = commands.Bot(command_prefix='!')

# set the openai api key
openai.api_key = '<YOUR_API_KEY>'

# set the rate limit
rate_limit = 0.3 #seconds

# listen for messages
@bot.event
async def on_message(message):
    #check if the message has the prefix
    if message.content.startswith('!openai'):
        #get the user input
        user_input = message.content[8:]
        #send the response
        response = openai.Completion.create(
            engine="davinci",
            prompt=user_input,
            max_tokens=50,
            temperature=0.9,
            top_p=1
        )
        await message.channel.send(response['choices'][0]['text'])

# run the bot
bot.run('<YOUR_DISCORD_BOT_TOKEN>')
