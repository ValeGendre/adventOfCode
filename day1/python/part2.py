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
calories_list.pop(idx)
idx, calories2 = max(calories_list, key=lambda x: x[1])
calories_list.pop(idx)
idx, calories3 = max(calories_list, key=lambda x: x[1])
print(calories1 + calories2 + calories3)
