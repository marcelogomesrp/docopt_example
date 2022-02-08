import os

from services.input_services import InputService

class FileInputService(InputService):
    def __init__(self, input_file:str) -> None:
        self._input_file = input_file

    def read_data(self) -> str:
        arquivo = open(self._input_file, 'r')
        content = arquivo.readlines()
        return content