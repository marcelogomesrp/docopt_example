import sys

from services.input_services import InputService

class StdioInputService(InputService):
    def __init__(self) -> None:
        pass

    def read_data(self) -> str:
        lines = sys.stdin.readlines()
        return lines