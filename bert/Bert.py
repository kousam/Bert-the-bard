
import discord
from discord import channel
from youtube_dl import YoutubeDL
from requests import get
from discord.ext import commands
from discord.utils import get

import asyncio
import traceback
import threading


from essentials.map import Map
from essentials.pen import Pen
from essentials.voice import Voice
#from mods.youtube import Youtube
#from mods.encyclopedia import Encyclopedia
#from mods.imposter import Imposter
#from mods.nuke import Nuke


from essentials.modLoader import ModLoader
from essentials.Context import Context


'''
Bert is a bot
'''


class Bert(discord.Client):
    

    DEFAULT_TEXT_CHANNEL = 'bert-commands'

    PREFIX = '.'

    def __init__(self):
        super().__init__()



        self.cmd_dict = {}

        self.voice_channel = None

        intents = discord.Intents.default()
        intents.members = True

        self.modLoader = ModLoader()

        self.map = Map(self)
        self.pen = Pen()
        self.voice = Voice(self)
        #self.youtube = Youtube(self)
        #self.encyclopedia = Encyclopedia(self)
        #self.imposter = Imposter(self)
        #self.nuke = Nuke(self)

        self.mods = {}

        self.addCommand('join', self.joinVC)

    def setToken(self, token):
        self.token = token
        

    async def run(self):
        
        try:
            self.log('BERT', 'Starting')
            await self.start(self.token)
        except:
            traceback.print_exc()
            await self.close()
            self.log('BERT', 'Invalid token')

    def isModLoaded(self, title):
        return title in self.mods
        

    # loads all mods from mods folder and adds the commands to cmd_dict
    def loadMods(self):
        self.mods = {}
        self.modLoader.loadMods()
        
        mod_lib = self.modLoader.getMods()

        for title, mod in mod_lib.items():
            print(title)
            loaded_mod = mod.init(self)
            mod_cmd = loaded_mod.getCommands()
            self.addAllCommands(mod_cmd)
            self.mods[title] = loaded_mod

            self.log('BERT' , 'Loaded mod: {}'.format(title))


    # add one command
    def addCommand(self, cmd, func):
        self.cmd_dict[cmd] = func

    # adds all commands given in cmd_dict
    def addAllCommands(self, cmd_dict):
        for cmd, func in cmd_dict.items():
            self.cmd_dict[cmd] = func

    # connect log output QTextEdit
    def setLogger(self, logger):
        self.logger = logger

    # appends text to log output QTextEdit
    def log(self, sender, text):
        try:
            self.logger.log(sender, text)
        except:
            pass

    
    # checks if message in specified default text channel
    def msgInDefaultChannel(self, msg):
        return msg.channel.name == self.DEFAULT_TEXT_CHANNEL


    async def runCommand(self, ctx, cmd, arg):
        if cmd in self.cmd_dict:
            func = self.cmd_dict[cmd]

            if arg == None:
                await func(ctx)

            else:
                await func(ctx, arg)

        else:
            self.log('BERT', 'Invalid command "{}"'.format(cmd))

        

    # string parsing for command
    # returns command title and argument
    def parseCommand(self, msg_str):
        # remove prefix
        msg_str = msg_str[1:] 
        msg_str_split = msg_str.split(' ', 1)

        if len(msg_str_split) == 1:
            cmd = msg_str_split[0]
            arg = None

        elif len(msg_str_split) >= 2:
            cmd = msg_str_split[0]
            arg = msg_str_split[1]

        else:
            cmd = None
            arg = None


        return cmd, arg




    async def on_ready(self):
        self.log('BERT', 'Logged in on Discord')


    async def on_message(self, msg):
        author = msg.author
        
        if author == self.user:
            return

        msg_str = msg.content
        
        if msg_str.startswith(self.PREFIX) and msg_str != self.PREFIX and self.msgInDefaultChannel(msg):
            cmd, arg = self.parseCommand(msg_str)

            ctx = Context(msg)

            await self.runCommand(ctx, cmd, arg)
            

    
    async def send(self, channel, msg):
        await channel.send(msg)


    async def joinMoveVC(self, target_vc):
        self.log('MAP','Attempting to join channel: {}'.format(target_vc.name))
        
        # if bert not in vc -> connect to vc
        # if bert in vc -> check if already in target_vc -> move if not
        # if target_vc == None -> dont do anything

        if self.voice_channel:
            if target_vc.id != self.voice_channel.id:
                self.voice_channel = target_vc
                await self.voice_channel.move()
                
        else:
            self.voice_channel = target_vc
            await self.voice_channel.connect()
                
            
        self.log('MAP','SUCCESS: Joined Channel: {}'.format(target_vc.name))
            



    async def joinVC(self, ctx):
        author = ctx.author

        if self.map.isInVoiceChannel(author):
            vc = author.voice.channel
            print(author)
            print(author.voice)
            print(author.voice.channel)

            await self.joinMoveVC(vc)

            self.voice.init(ctx.server)
    

    def setLoop(self, loop):
        self.loop = loop





        

        



