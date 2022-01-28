



class BertMod():
    def __init__(self, bert):
        self.bert = bert
        self.cmd_dict = {}

    def addCommand(self, cmd, func):
        self.cmd_dict[cmd] = func

    def getCommands(self):
        return self.cmd_dict

    def getBert(self):
        return self.bert






