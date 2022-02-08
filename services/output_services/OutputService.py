from abc import ABCMeta, abstractmethod

class OutputService:
    
    @abstractmethod
    def write(self) -> None:
        pass