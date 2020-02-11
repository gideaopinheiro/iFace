from Users.user import User

class Account:
    
    def __init__(self):
        self.user = self.createUser()
        self.friends = []
        self.messages = {}
    
    def createUser(self):
        userName = input("nome: ")
        password = input("senha: ")
        nickName = input("Como deseja ser chamado? ")
        newUser = User(userName, password, nickName)
        return newUser

    def getUser(self):
        return self.user
    
    def showFriends(self):
        for i in self.friends:
            print(i)
    
    def addFriend(self, user):
        self.friends.append(user)
    
    def __str__(self):
        return f'{self.getUser()}'
    