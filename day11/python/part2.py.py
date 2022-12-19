"""Use of decorator in python"""
from typing import Callable, List, Any, Tuple, Generator, Dict


def parse_monkey_input(
    text_prompt: str,
) -> Tuple[int, Generator[int, None, None], str, int, int, int]:
    """
    Parse the input prompt to parse data
    that will be useful for the Monkey class
    """

    monkey, starting_items, operation, *test = text_prompt.split("\n")
    monkey_id = int(monkey.split("Monkey ")[1].split(":")[0])
    starting_item_list = map(
        int, starting_items.strip().split("Starting items: ")[1].split(", ")
    )
    operation = operation[19:]
    test_op = int(test[0][21:])
    test_true = int(test[1][29:])
    test_false = int(test[2][30:])

    return monkey_id, starting_item_list, operation, test_op, test_true, test_false


class Monkey:
    "A Monkey"

    _id: int
    _item_list: List[int]
    _inspect: Callable[[int], int]
    _test: Callable[[int], bool]
    _give: Callable[[bool], int]
    _score: int = 0

    def __init__(self, prompt) -> None:
        (
            self._id,
            item_map,
            operation,
            self.test_op,
            test_true,
            test_false,
        ) = parse_monkey_input(prompt)
        self._item_list = list(item_map)
        self.parse_inpect_function(operation=operation)
        self._test = lambda item: item % self.test_op == 0
        self._give = lambda condition: test_true if condition else test_false

    def parse_inpect_function(self, operation: str) -> None:
        """Create the inspect operation"""
        list_op = operation.split(" ")
        match list_op[0]:
            case "old":
                default = lambda x: x
            case value if list_op[0].isdigit():
                default = lambda x: int(value)
            case _:
                raise ValueError

        if len(list_op) == 1:
            self._inspect = lambda worry_level: temp(worry_level)
            return

        for operator, new_variable in zip(list_op[1::2], list_op[2::2]):
            match new_variable:
                case "old":
                    temp2 = lambda x: x
                case value if new_variable.isdigit():
                    temp2 = lambda x: int(value)
                case _:
                    raise ValueError

            match operator:
                case "*":
                    temp = lambda x: default(x) * temp2(x)
                case "+":
                    temp = lambda x: default(x) + temp2(x)
                case "-":
                    temp = lambda x: default(x) - temp2(x)
                case _:
                    raise ValueError

        self._inspect = lambda worry_level: temp(worry_level)

    def turn(self) -> Dict[str, int]:
        """Simulate the turn of the monkey"""
        given_items = {
            self._give(True): [],
            self._give(False): [],
        }
        for item in self._item_list:
            new_worry_level = self._inspect(item)
            monkey_to_give = self._give(self._test(new_worry_level))
            given_items[monkey_to_give].append(new_worry_level)

        return given_items

    def add_items(self, item_list: List[int]):
        """Add monkey items to the new list"""
        self._item_list.extend(item_list)

    @property
    def id(self):
        """Getter for the id"""
        return self._id

    @property
    def score(self):
        """Getter for the score"""
        return self._score

    def __call__(self, item_list: List[int]) -> Any:
        self.add_items(item_list)
        self._score += len(self._item_list)
        given_items = self.turn()
        self._item_list = []
        return given_items

    def __repr__(self) -> str:
        return f"Monkey {self._id} : item_list = {self._item_list}"


INPUT_PROMPT_LIST: List[
    str
] = """Monkey 0:
  Starting items: 54, 89, 94
  Operation: new = old * 7
  Test: divisible by 17
    If true: throw to monkey 5
    If false: throw to monkey 3

Monkey 1:
  Starting items: 66, 71
  Operation: new = old + 4
  Test: divisible by 3
    If true: throw to monkey 0
    If false: throw to monkey 3

Monkey 2:
  Starting items: 76, 55, 80, 55, 55, 96, 78
  Operation: new = old + 2
  Test: divisible by 5
    If true: throw to monkey 7
    If false: throw to monkey 4

Monkey 3:
  Starting items: 93, 69, 76, 66, 89, 54, 59, 94
  Operation: new = old + 7
  Test: divisible by 7
    If true: throw to monkey 5
    If false: throw to monkey 2

Monkey 4:
  Starting items: 80, 54, 58, 75, 99
  Operation: new = old * 17
  Test: divisible by 11
    If true: throw to monkey 1
    If false: throw to monkey 6

Monkey 5:
  Starting items: 69, 70, 85, 83
  Operation: new = old + 8
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 7

Monkey 6:
  Starting items: 89
  Operation: new = old + 6
  Test: divisible by 2
    If true: throw to monkey 0
    If false: throw to monkey 1

Monkey 7:
  Starting items: 62, 80, 58, 57, 93, 56
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 6
    If false: throw to monkey 4""".split(
    "\n\n"
)

MONKEY_LIST: List[Monkey] = []
GIVING_LISTS: Dict[int, List[int]] = {}
MAX_MANAGEABLE_WORRY_LEVEL: int = 1
N = 10000

if __name__ == "__main__":
    for input_prompt in INPUT_PROMPT_LIST:
        MONKEY_LIST.append(Monkey(input_prompt))
        GIVING_LISTS[MONKEY_LIST[-1].id] = []

    for monkey in MONKEY_LIST:
        MAX_MANAGEABLE_WORRY_LEVEL *= monkey.test_op

    for i in range(N):
        print(f"{100*i/N:.2f} %")
        for monkey in MONKEY_LIST:
            give_items = monkey(GIVING_LISTS[monkey.id])
            GIVING_LISTS[monkey.id] = []
            for key in give_items:
                new_list = [
                    item % MAX_MANAGEABLE_WORRY_LEVEL for item in give_items[key]
                ]
                GIVING_LISTS[key].extend(new_list)

    print(list(map(lambda monkey: (monkey.id, monkey.score), MONKEY_LIST)))
