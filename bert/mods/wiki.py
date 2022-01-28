import wikipediaapi
from BertMod import BertMod


class Wiki(BertMod):
    def __init__(self, bert):
        super().__init__(bert)

        self.wikipedia = wikipediaapi.Wikipedia('en')

        self.addCommand('wiki', self.wiki)
    
        
    async def wiki(self, ctx, title):
        self.bert.log('MAP', 'Wiki request recieved "{}"'.format(title))
        page = self.wikipedia.page(title)
        
        if(page.exists()):
            self.bert.log('MAP', 'Found page "{}"'.format(page.title))
            self.bert.log('MAP', 'Sending summary for "{}" to channel "{}"'.format(page.title, ctx.channel.name))


            await self.bert.send(ctx.channel, 'Found "{}"'.format(page.title))
            await self.bert.send(ctx.channel, page.summary[0:2000])

        else:
            await self.bert.send('Could not find "{}"'.format(page.title))

        

def init(bert):
    e = Wiki(bert)
    return e
