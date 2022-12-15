from typing import Tuple, List, Dict

DIR_INPUTS : Dict[str, List[str]] = {}
MAX_SIZE : int = 100_000

def parse_input_prompt() -> None:
    temp = [line.split('$') for line in INPUT_PROMPT.split("$ ls")]
    for dir_info, content_info in zip(temp[:-1], temp[1:]):
        name = parse_dir_name(dir_info)
        content = parse_dir_content(content_info[0])
        if name in DIR_INPUTS: print(f'Dommage, {name =}')
        DIR_INPUTS[parse_dir_name(dir_info)] = parse_dir_content(content_info[0])

def parse_dir_name(dir_info : str) -> str:
    dir_name, _ = dir_info[-1].split('\n')
    return dir_name[4:]

def parse_dir_content(content_info: str) -> List[str]:
    content_list: List[str] = []
    for dir_content in content_info.split('\n'):
        if dir_content != '':
            content_list.append(dir_content)
    return content_list


class Tree:
    def __init__(self) -> None:
        self.root: Dir = {}
        self.root['/'] = Dir(name='/', content_info=DIR_INPUTS['/'], depth=0)

    def __repr__(self) -> str:
        return self.root['/'].__repr__()

class Dir:
    def __init__(self, name:str, content_info: List[str], depth: int = 0) -> None:
        self.visited = 0
        self.depth = depth
        self.name = name
        file_list, dir_list = self.parse_dir_input(content_info)
        self.child_nodes: Dict[str, Dir] = {}
        for child_name, child_content_info in dir_list:
            self.child_nodes[child_name] = Dir(
                child_name,
                child_content_info,
                depth=self.depth+1
            )
        self.files: Dict[str, File] = {}
        for file_name, file_size in file_list:
            self.files[file_name] = File(
                file_name,
                file_size,
                self.depth+1
            )

    def parse_dir_input(self, content_list :List[str]) -> Tuple[List[Tuple[str, int]], List[Tuple[str, List[str]]]]:
        file_list = []
        dir_list = []
        for content in content_list:
            node_type, name = content.split(' ')
            if node_type != 'dir':
                size = int(node_type)
                file_list.append((name, size))
            else :
                dir_list.append((name, DIR_INPUTS[name]))
        return file_list, dir_list
    
    @property
    def size(self) -> int:
        size = 0
        for file in self.files.values():
            size += file.size
        for dir in self.child_nodes.values():
            size += dir.size
        return size
        
    def __repr__(self) -> str:
        dir_repr = f"\033[92m{'  ' * self.depth} - {self.name} (dir, size={self.size})\033[0m\n" if self.size < MAX_SIZE else f"\033[91m{'  ' * self.depth} - {self.name} (dir, size={self.size})\033[0m\n"
        for file in self.files.values():
            dir_repr += f'{file}'
        for directories in self.child_nodes.values():
            dir_repr += f'{directories}'
        return dir_repr

class File:
    def __init__(self, name:str, size:int , depth:  int = 0) -> None:
        self.depth = depth
        self.name, self.size = name, size

    def __repr__(self) -> str:
        return f"{'  ' * self.depth}- {self.name} (file, size={self.size})\n"

def flatten_tree(tree : Tree):
    def flatten_dir(directory : Dir):
        flattened_dict : List[Tuple[str, int]] = []
        directory.visited += 1
        if directory.size < MAX_SIZE:
            flattened_dict.append(directory.size)
        for sub_dir in directory.child_nodes.values():
            flattened_dict += flatten_dir(sub_dir)
        return flattened_dict
    
    return flatten_dir(tree.root['/'])


if __name__=='__main__':
    with open(file='day7/ressources/input.txt') as f:
        INPUT_PROMPT = ''.join(f.readlines())
        parse_input_prompt()
        dir_tree = Tree()
        # MAX_SIZE = dir_tree.root['/'].size
        less_than_MAXSIZE_dir : Dict[str, int] = flatten_tree(dir_tree)
        # print(dir_tree)
        # print(f"{MAX_SIZE =}")
        # print(f"{sum(less_than_MAXSIZE_dir) =}")
        # # print(f"{sum(less_than_MAXSIZE_dir) =}")
        # for name, list_dir in DIR_INPUTS.items():
        #     print(name, list_dir)
