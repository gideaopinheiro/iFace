import sys
sys.path.append('..')

from Users.user import User
from Accounts.account import Account

users = []
accounts = []

def createUser():
    userName = input("Nome: ")
    password = input("Senha: ")
    nickName = input("Como deseja ser chamado? ")

    newUser = User(userName, password, nickName)
    users.append(newUser)
    return newUser

def createAccount(user: User):
    newAccount = Account(user)
    accounts.append(newAccount)

def getUsers():
    return users