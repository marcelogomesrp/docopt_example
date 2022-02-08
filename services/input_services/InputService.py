from abc import ABCMeta, abstractmethod

class InputService:

    @abstractmethod
    def read_data(self) -> str:
        pass