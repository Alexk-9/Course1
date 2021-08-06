from itertools import zip_longest
from json import dump

with open("users.csv", "r", encoding="utf-8") as users:
    with open("hobby.csv", "r", encoding="utf-8") as hobby:
        list_u_h = zip_longest(users, hobby)
        if len(users.readlines()) >= len(hobby.readlines()):
            users.seek(0)
            hobby.seek(0)
            dict_u_h = {n[0].replace(",", " ").strip(): str(n[1]).strip() for n in list_u_h}
            print(dict_u_h)
            with open("users_hobby.json", "w", encoding="utf-8") as f:
                dump(dict_u_h, f, ensure_ascii=False, indent=4)
        else:
            exit(1)
