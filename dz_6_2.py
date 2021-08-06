with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    rez1 = [n.split()[0] for n in f]
    dict_logs = {i: rez1.count(i) for i in rez1}
    print(f'Spamer {sorted(dict_logs.items(), key=lambda x: x[1])[-1]} times')

