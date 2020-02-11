from Users.user import User

class Account:
    
    def __init__(self, user: User):
        self.user = user
        self.chat = {}

    def getUser(self):
        return self.user

    
    def __str__(self):
        return f'{self.user.getNickName()}'
    