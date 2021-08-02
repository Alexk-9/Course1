src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

res = [src[r] for r in range(1, len(src)) if src[r] > src[r - 1]]

print(res)