class NumService:
    def __init__(self, data:list) -> None:
        self.next_line = 0        
        if(type(data) == str):
            self._data = data.split('\n')
        else:
            self._data = data

    def get_next_line(self) -> int:
        self.next_line += 1
        return self.next_line 
                

    def get_numerable_lines(self ) -> str:
        all_numerable_text = ""
        for line in self._data:
            all_numerable_text = all_numerable_text +  f'ln num: {self.get_next_line()} - {line}'

        return all_numerable_text


    
