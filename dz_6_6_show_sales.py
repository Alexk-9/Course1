from sys import argv

with open("bakery.csv", "r", encoding="utf-8") as f:
    if len(argv) == 3:
        start = int(argv[1])
        finish = int(argv[2])
        print(*(v for i, v in enumerate(f) if start -1 <= i < finish), sep='')
    elif len(argv) == 2:
        print(*(v for i, v in enumerate(f) if i >= int(argv[1])), sep='')
    else:
        print(f.read())