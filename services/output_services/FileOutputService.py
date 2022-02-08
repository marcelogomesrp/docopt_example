import os

from services.output_services import OutputService

class FileOutputService(OutputService):
    def __init__(self, output_file) -> None:
        if self._is_output_file_valid(output_file):
            self._output_file = output_file
        else:
            raise FileExistsError(f'The file {output_file} already exists')

    def _is_output_file_valid(self, output_file):
        return not os.path.exists(output_file)

    def write(self, data:str) -> str:
        #print(f'Wrinting content in file {self._output_file} -> {data}')
        with open(self._output_file, 'w') as file:
            file.write(data)
  