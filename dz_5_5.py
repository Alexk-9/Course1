src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

unique_src = [r for r in src if src.count(r) == 1]

print(unique_src)
