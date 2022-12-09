from typing import Tuple, List

DIR_INPUTS = {}

class Tree:
    def __init__(self, challenge_prompt: str) -> None:
        child_nodes = {}

class Dir:
    def __init__(self, dir_input_txt: str, challenge_prompt:str) -> None:
        self.child_nodes = {}

    def parse_dir_input(self, dir_input_txt:str) -> Tuple[List[Tuple(str, int)], List[Tuple(str, List[str])]]:
        content_list = dir_input_txt.split('\n')
        file_list = []
        dir_list = []
        for content in content_list:
            node_type, name = content.split(' ')
            if node_type != 'dir':
                size = int(node_type)
                file_list.append((name, size))
            else :
                new_dir_input_list = DIR_INPUTS[name]
        
    def __repr__(self) -> str:
        pass

class File:
    def __init__(self, file_input_txt: str) -> None:
        self.name, self.size = self.parse_file_input(file_input_txt)
    
    def parse_file_input(self, file_input_txt: str) -> Tuple[str, int]:
        name, size_str = file_input_txt.split(' ')
        return name, int(size_str)

    def __repr__(self) -> str:
        return f"{'  ' * self.depth}- {self.name} (file, size={self.size})"