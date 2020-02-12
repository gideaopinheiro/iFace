from Accounts.account import Account
from Users.user import User
from data import db


class UserMenu:
    
    def __init__(self, account: Account):
        self.account = account
        self.actions = {1: self.sendInvite, 2: self.editProfile, 3: self.resolveInvitations}
        self.execute()

    
    def execute(self):
        while True:
            self.showMenu()
            option = self.getOption()
            if option in range(1, len(self.actions) + 1):
                self.actions[option]()
            else:
                break
    

    # def sendMessageTo(self):
    #     who = input("Para quem deseja enviar uma mensagem? ")
    #     for u in self.friends:
    #         print(u)
    
    def resolveInvitations(self):
        self.account.getUser().displayInvitations()

    def sendInvite(self):
        nameUser = input("Quem você quer adicionar? ")
        users = db.getUsers()
        for i in  users:
            if(i.getUserNickName() == nameUser):
                i.invitation(self.account.getUser().getUserNickName())
    

    def showAccount(self):
        user = self.account.getUser()
        print(f"{user.getAge()}\n{user.getGender()}\n{user.getDescription()}\n\n")
    

    def searchUser(self, nickName: str):
        # for i in self.account.appen
        pass

    def showMenu(self):
        print("1: Enviar um convite    2: Editar perfil    3: Ver Convites")
    

    def getOption(self):
        option = int(input("-> "))
        return option
    

    def addUser(self):
        nameUser = input("Quem você quer adicionar? (Use o nome de usuário com '@') ")
        

    def editProfile(self):
        user = self.account.getUser()
        user.editProfile()
    