
class User:
    gender = 'Undefined'
    age = 'Undefined'
    description = ''


    def __init__(self, userName: str, password: str, nickName: str):
        self.userName = userName
        self.password = password
        self.nickName = nickName
        self.setProfile()
    
    def __str__(self):
       return f"{self.nickName}\n{self.age}\n{self.gender}\n{self.description}"
    
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