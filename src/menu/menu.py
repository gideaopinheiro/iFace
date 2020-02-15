from abc import ABC, abstractmethod



#Template Method
class Menu(ABC):

    def temlateMethod(self):
        self.execute()
        self.displayMenu()
    
    @abstractmethod
    def execute(self) -> None:
        pass

    @abstractmethod
    def displayMenu(self) -> None:
        pass