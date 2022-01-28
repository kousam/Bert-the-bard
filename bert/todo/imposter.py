import random


'''
Bert becomes the imposter and disconnects a random person


REQUIRES:
youtube mod
'''

class Imposter():
    URL = 'https://www.youtube.com/watch?v=r3eT9-B7cB0'

    def __init__(self, bert):
        self.bert = bert
        self.initCommands()


    async def sus(self, ctx):
        self.bert.log('IMPOSTER','Going for kill')

        if not self.bert.map.isInServer():
            await self.bert.map.joinWithCtx(ctx)
        else:
            await self.bert.map.joinVoiceChannel(ctx.author.voice.channel)

        await self.bert.youtube.forcePlay(self.URL, self.kill)
        members = self.bert.map.voice_channel.members
        randint = random.randint(0, len(members) -1)
        self.target = members[randint]

        self.bert.log('IMPOSTER', 'Target selected')
        


    async def kill(self):
        self.bert.log('IMPOSTER', 'Going for kill: {}'.format(self.target.name))
        await self.target.move_to(self.bert.map.getChannelByName('Samppes Wormhole'))
    

    def initCommands(self):
        @self.bert.client.command(pass_context=True)
        async def amogus(ctx):
            await self.sus(ctx)

