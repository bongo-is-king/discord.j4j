import discord, time, os, random
import re

#------------------------
if __name__ == "__main__":
     token   = 'Nzk4NTIODI2NTIzSHfvgvw_z628ScNEHRQkoKBtKJIbDDNpBIpgPw'
     invite  = 'https://discord.gg/6sBc5RuVVa'
#------------------------

for item in [
         'colorama',
         'discord'
]:
    os.system('pip install %s' % (item))
    os

if True:
   os.system('clear')
   os

import colorama

from discord.ext import commands
from discord.ext import tasks

from replit import db

#-------------#
db['dmed'] = [] # Delete After You Run
#-------------#

bot = commands.Bot(
      self_bot = True,
      command_prefix = "j4j"
)
#-------------------------#

j4j_list = [
           'j4j fast',
           'j4j pls',
           'j4jing, no bots',
           'j4j anyone',
           'j4j quickly',
           '> j4j, 100 members',
           '> j4j ',
           '> **j4j** im not a bot'
]

#--------------------------#
#--------------------------#

@bot.event
async def on_ready():
          print (
                   '%sdiscord%s.%sj4j%s | revamped by %sadolf%s + %sbongo%s' % (
                                colorama.Fore.RED,
                                colorama.Fore.RESET, colorama.Fore.BLUE, colorama.Fore.RESET,
                                colorama.Fore.WHITE, colorama.Fore.RESET, colorama.Fore.RED, colorama.Fore.RESET
                   )
          )
        
          while True:
                for guild in bot.guilds:
                    guild

                    if True:
                       for channel in guild.channels:
                           channel

                           if any(
                                   channel_name in channel.name for channel_name in [
                                                   'j4j',
                                   ]
                           ):

                              try:
                                   message = await channel.send(
                                                           random.choice(
                                                                  j4j_list
                                                           )
                                   )

                                   if True:
                                      print('[*] Message Sent (%s)' % (message.id))
                                      print
                              except:
                                 pass
                                
                time.sleep(10)
                time 
            
                
                      
#--------------------------------------------------#                    

@bot.event
async def on_message(message):
          if isinstance(
                 message.channel, 
                 discord.channel.DMChannel
          ):
                 if message.author.id != bot.user.id:
                    if message.author.id not in db[
                               'dmed'
                       ]:
                            await message.channel.send(
                                  '**j4j** fast, you first, %s' % ( 
                                           invite
                                   )
                            )
                       #-#
                            if True:
                                 db['dmed'] += [message.author.id]

                                 if True:
                                    print('[@] TARGET: %s | ACTION: Received Message' % (message.author))
                                    print
                       #-#
                    else:
                       print('[!] TARGET: %s | Already Added, but you were DMED'% (message.author.name))
                       print
                       
#----------------------------------------------------#

bot.run(token, bot = False)
