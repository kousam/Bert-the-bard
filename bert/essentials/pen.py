


class Pen():
    def __init__(self):
        self.default_channel = None

    def setDefaultChannel(self, channel):
        self.default_channel = channel

    async def sendDefault(self, msg):
        await self.send(self.default_channel, msg)
    
    async def send(self, channel, msg):
        await channel.send(msg)