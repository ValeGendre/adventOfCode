with open("ressources/input.txt") as f:
    calories_list = list(
        enumerate(
            [
                sum(list(map(int, temp.split("\n"))))
                for temp in "".join(f.readlines()).split("\n\n")
            ]
        )
    )

idx, calories1 = max(calories_list, key=lambda x: x[1])
print(calories1)
