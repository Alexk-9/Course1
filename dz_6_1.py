with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    list_log = [(line.split()[0], line.split()[5].replace('"', ''), line.split()[6]) for line in f]
    print(list_log)