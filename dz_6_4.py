from itertools import zip_longest

with open("users.csv", "r", encoding="utf-8") as users:
    with open("hobby.csv", "r", encoding="utf-8") as hobby:
        list_u_h = zip_longest(users, hobby)
        if len(users.readlines()) >= len(hobby.readlines()):
            users.seek(0)
            hobby.seek(0)
            with open("users_hobby.txt", "w", encoding="utf-8") as f:
                for n in list_u_h:
                    f.write(f'{n[0].strip()}: {str(n[1]).strip()}\n')
        else:
            exit(1)
