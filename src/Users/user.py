
from data import db
from Accounts.account import Account
from Communities.community import Community
from menu.util import formatNickName

class User:
    
    def __init__(self, userName, password, nickName):
        self.userName = userName
        self.password = password
        self.nickName = formatNickName(nickName)
        self.gender = 'Undefined'
        self.age = 'Undefined'
        self.description = ''
        self.chat = {}
        self.invitations = {}
        self.friends = []
        self.communities = []
        self.setProfile()
        self.displayInvitations()


    def __str__(self):
       return f"{self.nickName}\n{self.age}\n{self.gender}\n{self.description}"
    

    def newCommunity(self, owner, name, description):
        newCommunity = Community(owner, name, description)
        self.communities.append(newCommunity)
        return newCommunity


    def getCommunities(self):
        return self.communities


    def addCommunity(self, community):
        self.communities.append(community)


    def sendMessage(self, user, message):
        self.chat[user.getUserNickName()] = message
    

    def getMessages(self):
        return self.chat
    

    def invitation(self, user: Account):
        if user.getUser().getUserNickName() not in self.invitations:
            index = len(self.invitations) + 1
            self.invitations[index] = user
        else:
            return False
    

    def acceptInvitation(self, acc: Account, index: int):
        self.addFriend(acc)
        print(f"Você e {self.invitations[index].getUser().getUserNickName()} são amigos a partir de agora!\n")
        me = self.searchAccount(self.nickName)
        if me:
            acc.getUser().addFriend(me)
        del self.invitations[index]


    def rejectInvitation(self, index: int):
        del self.invitations[index]


    def addFriend(self, acc):
        self.friends.append(acc)


    def getFriends(self):
        return self.friends


    def displayInvitations(self):
        for i in list(self.invitations):
            print(f"{i}: {self.invitations[i].getUser().getUserNickName()}")
            accept = int(input("0: Rejeitar    1: Aceitar\n-> "))
            if accept==1:
                self.acceptInvitation(self.invitations[i], i)
            elif accept==0:
                self.rejectInvitation(i)
        if len(self.invitations) == 0:
            print("Não há convites no momento\n")
    

    def displayFriends(self):
        for i in range(len(self.friends)):
            print(f'{i+1}: {self.friends[i]}')


    def searchAccount(self, nickName: str):
        accounts = db.getAccounts()
        for i in accounts:
            if i.getUser().getUserNickName() == nickName:
                return i
        return False


    def setNickName(self):
        newNickName = input("Como quer ser chamado(a) ? ")
        self.nickName = "@"+newNickName
    

    def changePassword(self, newPassword: str):
        self.password = newPassword


    def getUserNickName(self):
        return self.nickName
    

    def getPassword(self):
        return self.password
    

    def setGender(self):
        genderOption = input("GÊNERO\nM: Masculino    F: Feminino    X: Prefino não informar\n").capitalize()
        if genderOption == 'M':
            self.gender = "M"
        elif genderOption == 'F':
            self.gender = "F"
        elif genderOption == 'X':
            self.gender = "Não informado"
    

    def getGender(self):
        return self.gender
    

    def setAge(self):
        userAge = input("IDADE:\n")
        if userAge:
            userAge = int(userAge)
            self.age = userAge


    def getAge(self):
        return self.age


    def setDescription(self):
        descp = input("DESCRIÇÃO\nFala um pouco sobre você:\n")
        self.description = descp 


    def getDescription(self):
        return self.description


    def setProfile(self):
        self.setAge()
        self.setGender()
        self.setDescription()


    def editProfile(self):
        while True:
            profileOptions = {1: self.setNickName, 2: self.setAge, 3: self.setGender, 4: self.setDescription}
            print(f"1) Nome de usuário: {self.nickName}\n2) Idade: {self.age}\n3) Sexo: {self.gender}\n4) Descrição: {self.description}\n5: Sair")
            option = int(input("-> "))
            if option in range(1, len(profileOptions)+1):
                profileOptions[option]()
            else:
                break

