"Part 2 of advent of code : day 7"

from typing import Tuple, List, Dict

CURRENT_DIRECTORY_PATH = []
DIR_INPUTS = {}

KEY = None
VALUE = []
SPACE_TO_FREE: int = 30_000_000
TOTAL_DISK_SPACE: int = 70_000_000


def parse_input_prompt() -> None:
    """Parse Input Prompt and create the drectory"""
    global KEY, VALUE
    for line in INPUT_PROMPT:
        match line.split(" "):
            case "$", "cd", "..":
                CURRENT_DIRECTORY_PATH.pop()
            case "$", "cd", directory:
                CURRENT_DIRECTORY_PATH.append(directory)
            case "$", "ls":
                if KEY is not None:
                    DIR_INPUTS[KEY] = VALUE
                KEY = "/".join(CURRENT_DIRECTORY_PATH)
                VALUE = []
            case "dir", directory:
                VALUE.append(f"dir {directory}")
            case size, file:
                VALUE.append(f"{size} {file}")
            case _:
                raise ValueError
    DIR_INPUTS[KEY] = VALUE


class Tree:
    "Root of the tree to Initialize the directory tree"

    def __init__(self) -> None:
        self.root: Dir = Dir(path="/", content_info=DIR_INPUTS["/"], depth=0)

    def __repr__(self) -> str:
        return self.root.__repr__()


class Dir:
    "Directory class that contains files & directory"

    def __init__(self, path: str, content_info: List[str], depth: int = 0) -> None:
        self.visited = 0
        self.depth = depth
        self.path = path
        file_list, dir_list = self.parse_dir_input(content_info)
        self.child_nodes: Dict[str, Dir] = {}
        for child_path, child_content_info in dir_list:
            child_dir = Dir(child_path, child_content_info, depth=self.depth + 1)
            self.child_nodes[child_dir.name] = child_dir
        self.files: Dict[str, File] = {}
        for file_name, file_size in file_list:
            self.files[file_name] = File(file_name, file_size, self.depth + 1)

    def parse_dir_input(
        self, content_list: List[str]
    ) -> Tuple[List[Tuple[str, int]], List[Tuple[str, List[str]]]]:
        "Parse the puzzle input to create a list of child nodes (dir & files)"
        file_list = []
        dir_list = []
        for content in content_list:
            node_type, name = content.split(" ")
            if node_type != "dir":
                size = int(node_type)
                file_list.append((name, size))
            else:
                path = "/".join([self.path, name])
                dir_list.append((path, DIR_INPUTS[path]))
        return file_list, dir_list

    @property
    def size(self) -> int:
        "Size of the directory"
        size = 0
        for file in self.files.values():
            size += file.size
        for dir in self.child_nodes.values():
            size += dir.size
        return size

    @property
    def name(self) -> str:
        "name of the directory"
        return self.path.split("/")[-1]

    def __repr__(self) -> str:
        dir_repr = (
            f"\033[92m{'  ' * self.depth} - {self.name} (dir, size={self.size})\033[0m\n"
            if self.size < 100_000
            else f"\033[91m{'  ' * self.depth} - {self.name} (dir, size={self.size})\033[0m\n"
        )
        for file in self.files.values():
            dir_repr += f"{file}"
        for directories in self.child_nodes.values():
            dir_repr += f"{directories}"
        return dir_repr


class File:
    "Class for a file"

    def __init__(self, name: str, size: int, depth: int = 0) -> None:
        self.depth = depth
        self.name, self.size = name, size

    def __repr__(self) -> str:
        return f"{'  ' * self.depth}- {self.name} (file, size={self.size})\n"


def flatten_tree(tree: Tree) -> List[Tuple[str, int]]:
    "Flatten the tree for all dir that have less than MAX_SIZE size."

    def flatten_dir(directory: Dir):
        flattened_dict: List[Tuple[str, int]] = []
        directory.visited += 1
        flattened_dict.append((directory.name, directory.size))
        for sub_dir in directory.child_nodes.values():
            flattened_dict += flatten_dir(sub_dir)
        return flattened_dict

    return flatten_dir(tree.root)


if __name__ == "__main__":
    with open(file="day7/ressources/input.txt", encoding="utf-8") as f:
        INPUT_PROMPT = "".join(f.readlines()).split("\n")
        parse_input_prompt()
        print(DIR_INPUTS)
        dir_tree = Tree()
        dir_list: List[Tuple[str, int]] = flatten_tree(dir_tree)
        print(dir_tree)
        free_space: int = TOTAL_DISK_SPACE - dir_tree.root.size
        space_needed: int = SPACE_TO_FREE - free_space
        print(f"{free_space = }")
        print(f"{space_needed = }")
        dir_list.sort(key=lambda x: x[1])
        filtered_list = filter(lambda x: x[1] > space_needed, dir_list)
        smallest_dir = next(filtered_list)
        print(f"Samellest Directory that will free up enough space : {smallest_dir}")
