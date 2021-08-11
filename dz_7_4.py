import os

import django
from collections import defaultdict

root_dir = django.__path__[0]
def_dict = defaultdict(int)
for root, dirs, files in os.walk(root_dir):
    for file in files:
        if os.stat(os.path.join(root, file)).st_size < 100:
            def_dict[100] += 1
        elif 100 <= os.stat(os.path.join(root, file)).st_size < 1000:
            def_dict[1000] += 1
        elif 1000 <= os.stat(os.path.join(root, file)).st_size < 10000:
            def_dict[10000] += 1
        elif 1000 <= os.stat(os.path.join(root, file)).st_size < 100000:
            def_dict[100000] += 1
        elif 10000 <= os.stat(os.path.join(root, file)).st_size < 1000000:
            def_dict[1000000] += 1
        elif 100000 <= os.stat(os.path.join(root, file)).st_size < 10000000:
            def_dict[10000000] += 1
        elif 1000000 <= os.stat(os.path.join(root, file)).st_size < 100000000:
            def_dict[100000000] += 1
for s, n in sorted(def_dict.items()):
    print(f'{s}: {n}')
