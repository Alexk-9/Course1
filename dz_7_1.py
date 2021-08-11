import os

folder = 'my_project'
folders = ['settings', 'mainapp', 'adminapp', 'authapp']

if not os.path.exists(folder):
    os.makedirs(folder)
    for i in folders:
        sub_folders = os.path.join(folder, i)
        os.makedirs(sub_folders)
else:
    print(f'{folder} Already exist')
    for i in folders:
        if os.path.exists(os.path.join(folder, i)):
            print(f'{i} exist')
        else:
            os.makedirs(os.path.join(folder, i))