#Importation :
import discord
import asyncio
from random import *
import listBot
import youtube_dl
import aiohttp
import os
import re
import logging

ws_url = 'ws://Guesser-Cluster.scoder12.repl.co'
guess_url = 'https://guess-it.scoder12.repl.co/guess'

client = discord.Client()

#"Roses are red\nViolets are Blue\n ---> Unxepected '{' at line 32", "What's the best thing about Switzerland?\n  ---> I don't know, but the flag is a big plus", "I invented  a new word\n ---> Plagiarism!",  "Did you hear about the mathematician who's afraid of big number?\n ---> He'll stop at nothing to avoid them", "Yesterday I saw a guy spill all his Scrabble letters on the road.\n ---> ---> I asked him,\n ---> What's the word on the street?","Knock! Knock!\n ---> Who is there?\n ---> Control freak.\n ---> Con...\n ---> Okay now you say,'Control freak who?'",

jokes = ["Quelle est la différence entre un porc et un rat ?\n ---> Aucun rapport", "Comment appelle-t-on un cochon qui rit ?\n ---> Un portugais",  "Que fait-on aux voleurs de salades ?\n ---> On laitue", "Pourquoi le patinage artistique est pénible ?\n ---> Car le patin agace", "Pourquoi quand on veut viser on ferme un œil ?\n ---> Car si on fermait les deux on verrait plus rien !", "Quel est le fromage préféré de Brigitte Macron ?\n ---> Le Président", "Comment les ours préfèrent-ils communiquer ?\n ---> Par E-miel", "Tu connais la blague du chauffeur de bus ?\n ---> Moi non plus, j’étais à l’arrière…", "Quel super héros donne le plus vite l’heure ?\n ---> Speed heure man !", "Un jour Dieu dit à Casto de ramer\n ---> Et depuis, castorama", "Qui fait 40 heures par semaine au bureau de poste ?\n ---> La machine à café", "Quel est le comble pour un dentiste ?\n ---> C’est d’habiter dans un palais", "Si tu jettes une imprimante dans l’eau…\n ---> Elle n'a papier", "Qu’est-ce qui est petit, carré et jaune ?\n ---> Un petit carré jaune!!!", "Pourquoi Harry Potter chuchotte ?\n ---> Parce que Dumbledore…", "C’est l’histoire d’une fleur qui court, qui court..\n ---> Et qui se plante", "Pourquoi les vieux font-ils des bains de boue?\n ---> Pour s’habituer à la terre…", "Docteur, je ne suis pas malade\n ---> Ca tombe bien, je ne suis pas docteur", "C'est l'histoire du ptit dej, tu la connais ?\n ---> Pas de bol", "C'est l'histoire d'un pingouin qui respire par les fesses\n ---> Un jour il s’assoit et il meurt", "C'est quoi une chauve souris avec une perruque ?\n ---> Une souris", "Que dit un escargot quand il croise une limace ?\n ---> Oh un naturiste", "Que fait un crocodile quand il rencontre une superbe femelle ?\n ---> Il Lacoste", "Quel est le point commun entre les maths et le sexe ?\n ---> Plus il y a d’inconnues, plus c’est chaud", "Tu connais la blague de la chaise\n ---> Ell est trop longue", "C'est l'histoire d'un papier qui tombe à l'eau...\n ---> Il crie « Au secours ! J’ai pas pied ! »", "Que fait une fraise sur un cheval ?\n ---> Tagada Tagada", "C'est l'histoire de 2 patates qui traversent la route\n ---> L’une d’elle se fait écraser. L’autre dit : « Oh purée ! »", "Une fesse gauche rencontre une fesse droite...\n ---> « Tu ne trouves pas que ça pue dans le couloir ? »", "Il y a 3 poussins dans un nid, j'en veux deux. Qu'est-ce que je fais ?\n ---> J’en pousse-un", "Qu'est ce qui n'est pas un steak ?\n ---> Une pastèque"]
''' EndListes ''' 


@client.event
async def on_ready():
  print("Bot en ligne")

@client.event
async def on_message(message):

  ''' Developpeur : '''

  if message.content == "?developper":
    em = discord.Embed(title="The Developper", descriptions="desc", colour=0xFF0000, timestamp=message.created_at)
    em.add_field(name="Remi_Mgt and Helife", value="Des gens cools ! 😀", inline = True)
    em.add_field(name="Ecrit en", value="Python 3.8.1", inline = True)
    em.set_footer(text = "Pour :  J'aime L'ail", icon_url=message.guild.icon_url)
    await message.channel.send(embed=em)
  
  ''' Blagues : '''

  if message.content.startswith("?blague"):
    lenght_jokes = len(jokes)-1
    new_message = await message.channel.send(jokes[randint(0, lenght_jokes)])

  ''' Messages divers : '''

  # Message = ?hello ou ?hi :
  if message.content == "?hello" or message.content == "?hi" :
    member_name = message.author.name
    guild_name = message.guild.name
    new_message = await message.channel.send("Hey " + member_name + " ,how are you ?")
    await new_message()
  
  # Message = ?coucou ou ?bonjour :
  if message.content == "?coucou" or message.content == "?bonjour" or message.content == "?salut" :
    member_name = message.author.name
    guid_name = message.guild.name
    new_message = await message.channel.send("Salut ! Comment vas-tu ?")

 # Message = ?bad ou mal :
  if message.content == "?bad" or message.content == "?mal" :
    member_name = message.author.name
    guid_name = message.guild.name
    new_message = await message.channel.send("Cheh !")

  # Message = ?bien ou good :
  if message.content == "?bien" or message.content == "?good" :
    member_name = message.author.name
    guid_name = message.guild.name
    new_message = await message.channel.send("Cool ! Comme moi !:)")


  # Message = ?help :
  if message.content == "?help" or message.content == "?commands" or message.content == "command" or message.content == "settings" :
    em = discord.Embed(title="Help", descriptions="desc", colour=0xFF0000, timestamp=message.created_at)
    em.add_field(name="?blague", value="Vous répond", inline = False)
    em.add_field(name="?Developper", value="Who is the developer?", inline = True)
    em.add_field(name="?hello ?hi ?bonjour ?coucou", value="Message de bienvenue", inline = False)
    em.add_field(name="?good ?bad ?bien ?mal", value="Vous répond", inline = False)
    em.set_footer(text = "Pour :  J'aime L'ail", icon_url=message.guild.icon_url)
    await message.channel.send(embed=em)


client.run("")
