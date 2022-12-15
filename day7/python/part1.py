"Part 1 of advent of code : day 7"

from typing import Tuple, List, Dict

CURRENT_DIRECTORY_PATH = []
DIR_INPUTS = {}

key = None
value = []
MAX_SIZE: int = 100_000


def parse_input_prompt() -> None:
    """Parse Input Prompt and create the drectory"""
    global key, value
    for line in INPUT_PROMPT:
        match line.split(" "):
            case "$", "cd", "..":
                CURRENT_DIRECTORY_PATH.pop()
                print(CURRENT_DIRECTORY_PATH)
            case "$", "cd", directory:
                CURRENT_DIRECTORY_PATH.append(directory)
                print(CURRENT_DIRECTORY_PATH)
            case "$", "ls":
                if key is not None:
                    DIR_INPUTS[key] = value
                key = "/".join(CURRENT_DIRECTORY_PATH)
                value = []
                print(key)
            case "dir", directory:
                value.append(f"dir {directory}")
                print(f"{directory} (dir)")
            case size, file:
                value.append(f"{size} {file}")
                print(f"{file} (file, size = {size})")
            case _:
                raise ValueError
    DIR_INPUTS[key] = value


class Tree:
    "Root of the tree to Initialize the directory tree"

    def __init__(self) -> None:
        self.root: Dir = {}
        self.root["/"] = Dir(path="/", content_info=DIR_INPUTS["/"], depth=0)

    def __repr__(self) -> str:
        return self.root["/"].__repr__()


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
            if self.size < MAX_SIZE
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


def flatten_tree(tree: Tree):
    "Flatten the tree for all dir that have less than MAX_SIZE size."

    def flatten_dir(directory: Dir):
        flattened_dict: List[Tuple[str, int]] = []
        directory.visited += 1
        if directory.size < MAX_SIZE:
            flattened_dict.append(directory.size)
        for sub_dir in directory.child_nodes.values():
            flattened_dict += flatten_dir(sub_dir)
        return flattened_dict

    return flatten_dir(tree.root["/"])


if __name__ == "__main__":
    with open(file="day7/ressources/input.txt", encoding="utf-8") as f:
        INPUT_PROMPT = "".join(f.readlines()).split("\n")
        parse_input_prompt()
        print(DIR_INPUTS)
        dir_tree = Tree()
        less_than_MAXSIZE_dir: Dict[str, int] = flatten_tree(dir_tree)
        print(dir_tree)
        print(f"{sum(less_than_MAXSIZE_dir) =}")
