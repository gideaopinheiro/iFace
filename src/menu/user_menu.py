from Accounts.account import Account

class UserMenu:
    
    def __init__(self, account: Account):
        self.account = account
        self.showAccount()
    
    def showAccount(self):
        user = self.account.getUser()
        print(f"{user.getAge()}\n{user.getGender()}\n{user.getDescription()}\n\n")
        self.account.showFriends()
        