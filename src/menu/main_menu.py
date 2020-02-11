from Accounts.account import Account
from .user_menu import UserMenu

class MainMenu:

    def __init__(self):
        self.options = {1: self.createAccount, 2: self.showUsers, 3: self.login}
        self.users = []
        self.execute()
    
    def execute(self):
        while True:
            self.displayMenu()
            action = int(input("-> "))
            if action in range(1, len(self.options) + 1):
                self.options[action]()
            else:
                break

    def displayMenu(self):
        print("1: Criar Conta\n2: Mostrar Usuários\n3: Login")
    
    def createAccount(self):
        newAccount = Account()
        self.users.append(newAccount)
        home = UserMenu(newAccount)

    
    def login(self):
        userInfo = self.getLoginInfo()
        if self.authenticateUser(userInfo):
            self.showWellcomeMessage(userInfo)
        else:
            print("usuario nao encontrado")
    
    def getLoginInfo(self):
        nickName = input("nome de usuario: ")
        password = input("senha: ")
        return [nickName, password]
        
    def authenticateUser(self, credential):
        for i in self.users:
            temp = i.getUser()
            if credential[0] == temp.getUserNickName() and credential[1] == temp.getPassword():
                return True
        return False
    
    def showWellcomeMessage(self, user):
        print(f"Bem vindo(a), {user[0]}")
    
    def showUsers(self):
        for i in self.users:
            print(i)