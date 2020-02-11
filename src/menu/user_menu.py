from Accounts.account import Account
from Users.user import User

class UserMenu:
    
    def __init__(self, account: Account):
        self.account = account
        self.friends = []
        self.actions = {1: self.addFriend, 2: self.editProfile}
        self.execute()

    
    def execute(self):
        while True:
            self.showMenu()
            option = self.getOption()
            if option in range(1, len(self.actions) + 1):
                self.actions[option]()
            else:
                break
    

    def sendMessageTo(self):
        who = input("Para quem deseja enviar uma mensagem? ")
        for u in self.friends:
            print(u)
    

    def addFriend(self, user: User):
        self.friends.append(user)
    

    def showAccount(self):
        user = self.account.getUser()
        print(f"{user.getAge()}\n{user.getGender()}\n{user.getDescription()}\n\n")
    

    def searchUser(self, nickName: str):
        # for i in self.account.appen
        pass

    def showMenu(self):
        print("1: Fazer uma amizade    2: Editar perfil    3: Enviar uma mensagem    4: Sair")
    

    def getOption(self):
        option = int(input("-> "))
        return option
    

    def addUser(self):
        nameUser = input("Quem você quer adicionar? (Use o nome de usuário com '@') ")
        

    def editProfile(self):
        user = self.account.getUser()
        user.editProfile()
    

