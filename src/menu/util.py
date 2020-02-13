
def formatNickName(nickName):
    return nickName if nickName[0] == '@' else '@'+nickName

def showWellcomeMessage(self, user: list):
    print(f"Bem vindo(a), {user[0]}")