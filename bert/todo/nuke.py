import random


'''
Bert gets a 25 kill killstreak and send a nuke
everyone goes flying around the server 


REQUIRES:
youtube mod
'''

class Nuke():
    URL = 'https://www.youtube.com/watch?v=2TWa9JklTgs'

    def __init__(self, bert):
        self.bert = bert
        self.initCommands()


    async def run(self, ctx):
        self.bert.log('NUKE','INCOMING')

        if not self.bert.map.isInServer():
            await self.bert.map.joinWithCtx(ctx)
        else:
            await self.bert.map.joinVoiceChannel(ctx.author.voice.channel)

        await self.bert.youtube.forcePlay(self.URL, self.boom)


    async def boom(self):
        self.bert.log('NUKE','BOOM')

        members = self.bert.map.voice_channel.members
        channels = self.bert.map.getAllVoiceChannels()

        for member in members:
            randint = random.randint(0, len(channels) -1)
            channel = channels[randint]
            await member.move_to(channel)


    def initCommands(self):
        @self.bert.client.command(pass_context=True)
        async def nuke(ctx):
            if self.bert.validate(ctx):
                await self.run(ctx)