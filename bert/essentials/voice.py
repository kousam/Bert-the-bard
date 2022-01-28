


class Voice():
    def __init__(self, bert):
        self.bert = bert
        self.voice_client = None
    
    def init(self, server):
        self.voice_client = server.voice_client
        self.bert.log('LUTE', 'Setting voice client on server {}'.format(server.name))

    def on_leave(self):
        self.voice_client = None

    def exists(self):
        return self.voice_client != None

    def grab(self):
        return self.voice_client

    def is_playing(self):
        return self.voice_client.is_playing()

    def is_paused(self):
        return self.voice_client.is_paused()

    def play(self, audio, _after):
        self.voice_client.play(audio, after=_after)

    def stop(self):
        if self.exists():
            self.voice_client.stop()

    def pause(self):
        if self.exists():
            self.voice_client.pause()

    def resume(self):
        if self.exists():
            self.voice_client.resume()

    


