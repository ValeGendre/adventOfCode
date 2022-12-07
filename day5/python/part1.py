"""Part 1 of Advent of code 2022 Day 5"""

from typing import List, Tuple


def truncate_state_from_command(input_text) -> Tuple[str, List[str]]:
    """
    returns a Tuple, the first element is the initial state,
    the second element is the commands to do on this state
    """
    text_initial_state, commands = input_text.split("\n\n")
    return text_initial_state, commands.split("\n")


class Stack:
    """One stack is a list of the crate names"""

    def __init__(self, crate_list: List[str]) -> None:
        self.crates = crate_list

    def add_crate(self, create_name: str) -> None:
        "Add crate crate_name to the crate list"
        self.crates.append(create_name)

    def remove_crate(self, number_to_remove: int) -> List[str]:
        "Remove the number_to_remove crate(s) to the crate list and returns them"
        removed_crates = []
        for _ in range(number_to_remove):
            removed_crates.append(self.crates[-1])
            self.crates.pop(-1)
        return removed_crates

    def __repr__(self) -> str:
        if len(self.crates) == 0:
            return " "
        return "".join(self.crates)


class Stacks:
    """Class of all stacks"""

    def __init__(self, initial_input_state: List[str]) -> None:
        self.stack_list = [
            Stack(crate_list) for crate_list in Stacks.parse_input(initial_input_state)
        ]

    @staticmethod
    def parse_input(input_text: str) -> List[List[str]]:
        """
        Parse the problem input to create the crates list,
        returns the number of stacks (len of the list) and a crate list
        """
        *crate_text_list, crate_number = input_text.split("\n")
        input_text_list = crate_number.strip().split("   ")
        crate_stack_list = [[] for _ in input_text_list]
        for stage in crate_text_list:
            for idx in range(len(input_text_list)):
                crate_list_idx = 4 * (idx + 1) - 3
                crate_name = stage[crate_list_idx]
                if crate_name != " ":
                    crate_stack_list[idx] = [stage[crate_list_idx]] + crate_stack_list[
                        idx
                    ]
        return crate_stack_list

    def move_crate(self, movement: str) -> None:
        "Move crates according to the movement read from the problem input"
        number_of_crate, stack_origin, stack_destination = Stacks.parse_command(
            movement
        )
        crate_to_move = self.stack_list[stack_origin].remove_crate(number_of_crate)
        for crate in crate_to_move:
            self.stack_list[stack_destination].add_crate(crate)

    @staticmethod
    def parse_command(command: str) -> Tuple[int, int, int]:
        """
        Parse the command input into a tuple
        (number of crates, stack origin, stack destination)
        """
        number_of_crate, rest = command[5:].split(" from ")
        stack_origin, stack_destination = rest.split(" to ")
        return int(number_of_crate), int(stack_origin) - 1, int(stack_destination) - 1

    def score(self) -> str:
        "Returns the last crate of each stack"
        last_crates = []
        for stack in self.stack_list:
            if len(stack.crates) != 0:
                last_crates.append(stack.crates[-1])
        return "".join(last_crates)

    def __repr__(self) -> str:
        return self.stack_list.__repr__()


if __name__ == "__main__":

    with open("day5/ressources/input.txt", encoding="utf-8") as f:
        RAW_INPUT_TEXT = "".join(f.readlines())

    initial_state, command_list = truncate_state_from_command(RAW_INPUT_TEXT)
    s = Stacks(initial_state)
    for command_movement in command_list:
        s.move_crate(command_movement)
    print(s.score())
