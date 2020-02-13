from Accounts.account import Account
from Users.user import User
from Communities.community import Community
from menu.community_menu import CommunityMenu
from data import db

from .util import formatNickName

class UserMenu:
    
    def __init__(self, account: Account):
        self.account = account
        self.actions = {1: self.sendInvite, 2: self.resolveInvitations, 3: self.editProfile, 4: self.showFriends, 5: self.communities }
        self.execute()


    def communities(self):
        while True:
            act = int(input("1: Mostrar comunidades    2: Criar comunidade    3: Voltar\n-> "))
            if act == 1:
                myCommunities = db.getCommunities()
                for i in range(len(myCommunities)):
                    print(f"{i+1}: {myCommunities[i]}\n")
            elif act == 2:
                self.createCommunity()
            else:
                break



    def createCommunity(self):
        communityName = input("Nome da comunidade: ")
        description = input(f"Faça uma pequena descrição sobre a {communityName}\n")
        cmnt = db.createCommunity(self.account.getUser(), communityName, description)
        CommunityMenu(cmnt, self.account.getUser())
    
    def execute(self):
        while True:
            self.showMenu()
            option = self.getOption()
            if option in range(1, len(self.actions) + 1):
                self.actions[option]()
            else:
                break
    
    
    def resolveInvitations(self):
        self.account.getUser().displayInvitations()


    def sendInvite(self):
        nameUser = input("Quem você quer adicionar? ")
        nameUser = formatNickName(nameUser)
        accounts = db.getAccounts()
        for i in  accounts:
            if(i.getUser().getUserNickName() == nameUser):
                i.getUser().invitation(self.account)
                break
    

    def showAccount(self):
        user = self.account.getUser()
        print(f"{user.getAge()}\n{user.getGender()}\n{user.getDescription()}\n\n")
    

    def showFriends(self):
        self.account.getUser().displayFriends()


    def showMenu(self):
        print("\n1: Enviar um convite    2: Ver Convites    3: Editar perfil    4: Ver amigos    5: Criar comunidade    6: Sair")
    

    def getOption(self):
        option = int(input("-> "))
        return option
    

    def addUser(self):
        nameUser = input("Quem você quer adicionar? (Use o nome de usuário com '@') ")
        

    def editProfile(self):
        user = self.account.getUser()
        user.editProfile()
    