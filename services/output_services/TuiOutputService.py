
from services.output_services import OutputService, FileOutputService

class TuiOutputService(OutputService):
    def __init__(self) -> None:
        pass

    def write(self, data:str) -> str:
        output_file = input('Entre com o arquivo de destino: ')        
        fileOutputService = FileOutputService(output_file)
        fileOutputService.write(data)        