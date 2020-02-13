import sys
sys.path.append('..')


class Account:
    
    def __init__(self, user):
        self.user = user
        self.communities = []
        self.chat = {}


    def getUser(self):
        return self.user

    
    def __str__(self):
        return f'{self.user.getUserNickName()}'
    