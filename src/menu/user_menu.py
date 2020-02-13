from Accounts.account import Account
from Users.user import User
from Communities.community import Community
from menu.community_menu import CommunityMenu
from data import db

from .util import formatNickName

class UserMenu:
    
    def __init__(self, account: Account):
        self.account = account
        self.actions = {1: self.sendInvite, 2: self.resolveInvitations, 3: self.editProfile, 4: self.showFriends, 5: self.communities, 6: self.sendMessage, 7: self.readMessagess }
        self.execute()


    def execute(self):
        while True:
            self.showMenu()
            option = self.getOption()
            if option in range(1, len(self.actions) + 1):
                self.actions[option]()
            else:
                break
    
	
    def sendMessage(self):
        nameUser = input("Para quem deseja enviar uma mensagem? ")
        nameUser = formatNickName(nameUser)
        users = self.account.getUser().getFriends()
        for user in  users:
            if(user.getUser().getUserNickName() == nameUser):
                message = input("\nEscreva a sua mensagem abaixo e pressione Enter para enviar\n-> ")
                user.getUser().sendMessage(self.account.getUser(), message)
                return True
        print(f"\nVocê precisa tornar-se amigo de {nameUser} antes de enviar uma mensagem\n")
    
    def readMessagess(self):
        messages = self.account.getUser().getMessages()
        for i in messages:
            print(f"{i} disse: {messages[i]}")


    def communities(self):
        while True:
            act = int(input("1: Mostrar comunidades    2: Criar comunidade    3: Voltar\n-> "))
            if act == 1:
                myCommunities = self.account.getUser().getCommunities()
                for i in range(len(myCommunities)):
                    print(f"{i+1}: {myCommunities[i]}\n")
            elif act == 2:
                self.createCommunity()
            else:
                break


    def createCommunity(self):
        communityName = input("Nome da comunidade: ")
        description = input(f"Faça uma pequena descrição sobre a {communityName}\n")
        cmnt = self.account.getUser().newCommunity(self.account.getUser(), communityName, description)
        CommunityMenu(cmnt, self.account.getUser())
    
    
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
        print("\n1: Enviar um convite    2: Ver Convites    3: Editar perfil    4: Ver amigos    5: Comunidades    6: Enviar Mensagem    7: Ver Mensagens    8: Sair")
    

    def getOption(self):
        option = int(input("-> "))
        return option
    

    def editProfile(self):
        user = self.account.getUser()
        user.editProfile()
    