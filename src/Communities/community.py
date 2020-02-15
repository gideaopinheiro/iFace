
class Community:
    
    def __init__(self, owner, name, description):
        self.owner = owner
        self.name = name
        self.description = description
        self.members = []


    def __str__(self):
        return f"{self.name}\n{self.owner}"


    def getOwner(self):
        return self.owner


    def setName(self, newName):    
        self.name = newName


    def getName(self):
        return self.name


    def setDescription(self, newDescription):
        self.description = newDescription


    def addMember(self, newMember):
        self.members.append(newMember)
    

    def removeMember(self, member):
        for i in range(self.members):
            if self.members[i].getUserNickName() == member.getUserNickName():
                del self.members[i]
    

    def newMessage(self, user, message):
        for member in self.members:
            member.sendMessage(user, message)
    

    def displayMembers(self):
        for i in self.members:
            print(i.getUserNickName())