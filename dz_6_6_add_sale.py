from sys import argv

with open("bakery.csv", "a", encoding="utf-8") as f:
    if argv[1].replace('.', '').replace(',', '').isdigit():
        print(f"{round(float(argv[1].replace(',', '.')), 3):>015}", file=f)
    else:
        print("Enter correct number")