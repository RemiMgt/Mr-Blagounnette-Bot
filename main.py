import discord
import asyncio
from random import *
import listBot

ws_url = 'ws://Guesser-Cluster.scoder12.repl.co'
guess_url = 'https://guess-it.scoder12.repl.co/guess'

client = discord.Client()

''' Listes : ''' 
BAN_WORDS  = ["connard", "con", "fdp", "conne", "débile","php","css","html", "fils de pute", "fuke", "fuk", "ta grand mère"]

jokes = ["Roses are red\nViolets are Blue\n---> Unxepected '{' at line 32","Quelle est la différence entre un porc et un rat ?\n---> Aucun rapport", "Comment appelle-t-on un cochon qui rit ?\n---> Un portugais", "What's the best thing about Switzerland?\n ---> I don't know, but the flag is a big plus", "I invented  a new word\n ---> Plagiarism!", "Did you hear about the mathematician who's afraid of big number?\n---> He'll stop at nothing to avoid them", "Yesterday I saw a guy spill all his Scrabble letters on the road.\n ---> ---> I asked him,\n ---> What's the word on the street?","Knock! Knock!\n---> Who is there?\n---> Control freak.\n---> Con...\n---> Okay now you say,'Control freak who?'"]
''' EndListes ''' 


@client.event
async def on_ready():
  print("Bot en ligne")

@client.event
async def on_message(message):
  if message.author != client.user :
    for word in BAN_WORDS:
      if word in message.content.lower():
        await message.delete()
        await message.author.send("Désolé c'est pas trés gentil de dire  : " + word)

  if message.content == "?developper":
    em = discord.Embed(title="The Developper", descriptions="desc", colour=0xFF0000, timestamp=message.created_at)
    em.add_field(name="Remi_Mgt and Helife", value="A cool man", inline = True)
    em.add_field(name="Ecrit en", value="Python 3.8.1", inline = True)
    em.set_footer(text = "Pour un super serveur", icon_url=message.guild.icon_url)
    await message.channel.send(embed=em)
  
  if message.content == "?hello":
    member_name = message.author.name
    guild_name = message.guild.name
    new_message = await message.channel.send("Hey " + member_name)
    await new_message()
  if message.content.startswith("?blague"):
    lenght_jokes = len(jokes)-1
    new_message = await message.channel.send(jokes[randint(0, lenght_jokes)])
  
  if message.content == "?ping" :
    new_message = await message.channel.send("Test")

  if message.content == "?help" or message.content == "?command":
    em = discord.Embed(title="Help", descriptions="desc", colour=0xFF0000, timestamp=message.created_at)
    em.add_field(name="?Developper", value="Who is the developer?", inline = True)
    em.add_field(name="?hello", value="Say Hello", inline = False)
    em.set_footer(text = "Pour un super serveur", icon_url=message.guild.icon_url)
    await message.channel.send(embed=em)

client.run("NjkzNTQyMjMwMjM2OTg3NTUy.Xn-mAw.XXaDG0T5Oj9ZyCuazKthpG9aEZs")