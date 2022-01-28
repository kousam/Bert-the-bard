
import discord
from youtube_dl import YoutubeDL
from requests import get
from discord.utils import get

from essentials.callback import Callback

from BertMod import BertMod

'''

Mod for playing playing music through youtube

REQUIRES:
Lute

'''


class Youtube(BertMod):
    FFMPEG_OPTS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}

    def  __init__(self, bert):
        super().__init__(bert)
   
        self.queue_list = []

        self.addCommand('play', self.queue)
        self.addCommand('pause', self.pause)
        self.addCommand('resume', self.resume)
        self.addCommand('stop', self.stop)
        self.addCommand('skip', self.skip)
        


    def load(self, url):
        title, source = self.search(url)
        return title, source

    

    async def queue(self, ctx, url):
        self.getBert().log('YOUTUBE', 'Queue request: {}'.format(url))
        title, source = self.load(url)
        self.queue_list.append([ctx, title, source])

        await self.getBert().send(ctx.channel, 'Queued: "{}"'.format(title))

        if not self.bert.voice.is_playing() and len(self.queue_list) == 1:
            await self.playNext()


    async def playNext(self):
        if len(self.queue_list) > 0:
            ctx, title, source = self.queue_list.pop(0)

            audio = discord.FFmpegPCMAudio(source, **self.FFMPEG_OPTS)
            callback = Callback(self.bert, self.playNext).call

            self.getBert().log('YOUTUBE', 'Playing: {}'.format(title))

            self.getBert().voice.play(audio, callback)

            

    async def forcePlay(self, url, after):
        self.getBert().log('YOUTUBE', 'FORCE Play request')
        if self.getBert().voice.is_playing:
            self.getBert().voice.stop()
            self.clear()

        title, source = self.load(url)
        audio = discord.FFmpegPCMAudio(source, **self.FFMPEG_OPTS)
        callback = Callback(self.bert, after).call

        self.getBert().log('YOUTUBE', 'FORCE Playing: {}'.format(title))
        self.getBert().voice.play(audio, callback)

        


    async def stop(self, ctx):
        if self.getBert().voice.is_playing():
            self.getBert().voice.stop()
            self.getBert().log('YOUTUBE', 'STOPPED')



    async def pause(self, ctx):
        if self.bert.voice.is_playing():
            self.bert.voice.pause()
            self.bert.log('YOUTUBE', 'PAUSED')


    async def resume(self, ctx):
        if self.bert.voice.is_paused():
            self.bert.voice.resume()
            self.bert.log('YOUTUBE', 'RESUMED')


    async def skip(self, ctx):
        self.bert.log('YOUTUBE', 'Skipping')
        await self.stop(ctx)

        await self.playNext()


    def clear(self):
        self.bert.log('YOUTUBE', 'Queue Cleared')
        self.queue_list = []


    def search(self, url):
        
        with YoutubeDL({'quiet':'True','format': 'bestaudio', 'noplaylist':'True'}) as ydl:
            try: 
                requests.get(url)
            except: 
                info = ydl.extract_info(f"ytsearch:{url}", download=False)['entries'][0]

            else: info = ydl.extract_info(url, download=False)

        self.bert.log('YOUTUBE', 'Found {}'.format(info['title']))

        return (info['title'], info['formats'][0]['url'])




def init(bert):
    y = Youtube(bert)
    return y

