import discord
import os
import requests
import json
import random
from replit import db
from keep_alive import keep_alive

client=discord.Client()

sad_words= ["sad","depressed","unhappy","miserable","unalive","kill","die"]

starter_encouragements=[
  "cheer up!!",
  "Hang in there.",
  "You are a great person!"
]

def get_quote():
  response= requests.get("https://zenquotes.io/api/random")
  json_data=json.loads(response.text)
  quote=json_data[0]['q']+" -"+json_data[0]['a']
  return quote

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event 
async def on_message(message):

  msg=message.content
  if message.author==client.user :
    return
  if message.content.startswith('!Hello'):
    await message.channel.send('Hello!')
  if message.content.startswith('!hello'):
    await message.channel.send('Hello!')
  if message.content.startswith("!inspire"):
    quote=get_quote()
    await message.channel.send(quote)

  if any(word in msg for word in sad_words):
    await message.channel.send(random.choice(starter_encouragements))

keep_alive()
client.run(os.getenv('TOKEN'))
    
  
