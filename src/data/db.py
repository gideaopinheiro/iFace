
from Users import user
from Accounts.account import Account
from Communities.community import Community


users = []
accounts = []
communities = []

def createUser():
    userName = input("Nome: ")
    password = input("Senha: ")
    nickName = input("Como deseja ser chamado? ")

    newUser = user.User(userName, password, nickName)
    users.append(newUser)
    return newUser


def createAccount(user):
    newAccount = Account(user)
    accounts.append(newAccount)
    return newAccount


# def createCommunity(owner, name, description):
    

def getCommunities():
    return communities

def getUsers():
    return users


def getAccounts():
    return accounts