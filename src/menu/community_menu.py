from Communities.community import Community
from data import db
from Users.user import User


class CommunityMenu:

    def __init__(self, community: Community, me: User):
        self.options = {1: self.displayMembers, 2: self.addMember, 3: self.removeMember, 4: self.sendMessage, 5: self.readMessages}
        self.community = community
        self.owner = community.getOwner()
        self.me = me
        self.execute()


    def execute(self):
        while True:
            self.showMenu()
            act = int(input("-> "))
            if act in range(1, len(self.options)+1):
                self.options[act]()
            else:
                break


    def displayMembers(self):
        self.community.displayMembers()


    def showMenu(self):
        print(f"Bem vindo a comunidade {self.community.getName()}")
        print("\n1: Ver membros    2: Adicionar um membro    3: Remover um membro    4: Enviar mensagem na comunidade    5: Ler mensagens    6: Voltar")
    

    def addMember(self):
        if self.me.getUserNickName() == self.owner.getUserNickName():
            userName = input("Quem você deseja adicionar? ")
            users = db.getUsers()
            for user in users:
                if user.getUserNickName() == userName:
                    self.community.addMember(user)
                    return True
            print("Usuário não existe")
        else:
            print("Somente o administrador pode executar esta ação!")

    
    def removeMember(self):
        userName = input("Quem você deseja deletar? ")
        users = db.getUsers()
        for user in users:
            if user.getUserNickName() == userName:
                self.community.removeMember(user)
    

    def sendMessage(self):
        ... 
    

    def readMessages(self):
        ... 
