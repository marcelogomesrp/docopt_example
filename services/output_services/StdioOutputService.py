import sys

from services.output_services import OutputService

class StdioOutputService(OutputService):
    def __init__(self) -> None:
        pass

    def write(self, data:str) -> str:
        print(data)