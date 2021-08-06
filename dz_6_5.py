from itertools import zip_longest
from sys import argv

users, hobby, us_hob = argv[1:]

with open("users", "r", encoding="utf-8") as us:
    with open("hobby", "r", encoding="utf-8") as hob:
        list_u_h = zip_longest(us, hob)
        if len(us.readlines()) >= len(hob.readlines()):
            us.seek(0)
            hob.seek(0)
            with open("us_hob.txt", "w", encoding="utf-8") as f:
                for n in list_u_h:
                    f.write(f'{n[0].strip()}: {str(n[1]).strip()}\n')
        else:
            exit(1)