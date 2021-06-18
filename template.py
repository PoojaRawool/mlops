# template.py file is going to create all the required files and folders in your current working directory.

import os
# when we will be creating files we need certain directories(dirs)
# we are using os.path.join because / or \ can create error so based on your os it will join the path
# data is the base directory and raw is the child directory
dirs = [
        os.path.join("data","raw"),
        os.path.join("data","processed"),
        "notebooks",
        "saved_models",
        "src"
      ]
# we will create these directory structures one by one
for dir_ in dirs:
    os.makedirs(dir_, exist_ok=True)
    # exist_ok=True: if the folder is already created it wont throw any error
    # each folder will be containing .gitkeep file
    with open(os.path.join(dir_, ".gitkeep"),"w") as f:
        pass

# we will also creating files in those directories(files)
files = [
        "dvc.yaml",
        "params.yaml",
        ".gitignore",
        os.path.join("src","__init.py__")
      ]
# now we will be just opening these files and saving it
for file_ in files:
    with open(file_,"w") as f:
        pass
    