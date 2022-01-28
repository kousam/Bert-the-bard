import os

TOKEN_PATH = 'token.txt'


class FileMgr():




    def getToken():
        with open(TOKEN_PATH, 'r') as file:
            lines = file.readlines()

        token = lines[0]
        return token

    def saveToken(token):
        with open(TOKEN_PATH, 'w') as file:
            file.write(token)
            file.close()




