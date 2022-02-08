#from services import FileService, InputService

from services.input_services import InputService, FileInputService

class TuiInputService(InputService):
    def __init__(self) -> None:
        pass

    def read_data(self) -> str:
        input_file = input('Entre com o arquivo de origem: ')        
        print(f"read from tui class input {input_file}")
        fileInputService = FileInputService(input_file)
        return fileInputService.read_data()
