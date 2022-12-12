import os
import shutil

def manageFolder(name: str):
    if not os.path.exists(f'./{name}'):
        os.mkdir(f'./{name}')
    else:
        shutil.rmtree(f'./{name}')  # 等效於 rm -rf ./name
        os.mkdir(f'./{name}')
