


'''
Berts trusty old map to guide him through server channels


'''

class Map():
    def __init__(self, bert):
        self.bert = bert




    def isInVoiceChannel(self, target):
        return target.voice != None

    def inSameVoiceChannel(self, comp1, comp2):
        value = False
        
        if self.isInVoiceChannel(comp1) and self.isInVoiceChannel(comp2):
            if comp1.channel.id == comp2.channel.id:
                value = True
        
        return value


    def getServer(self):
        return self.server

    def getAllVoiceChannels(self):
        return self.server.voice_channels

    def getChannelByName(self, name):
        target_channel = None

        for channel in self.server.channels:
            if channel.name == name:
                target_channel = channel

        return target_channel

    async def disconnect(self):
        self.bert.log('MAP','Disconnecting')

        self.bert.lute.grab().disconnect()


    def getMembersByName(self, channel):
        pass



















