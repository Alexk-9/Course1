import os
import shutil

root_dir = 'my_project_1'

for root, dirs, files in os.walk(root_dir):
    for dir_t in dirs:
        if dir_t == 'templates':
            shutil.copytree(os.path.join(root, dir_t), os.path.join(root_dir, 'templates'), dirs_exist_ok=True)
