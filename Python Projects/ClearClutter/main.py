import os

print("Welcome to Clear The Clutter")
while True:
    try:
        directory = input(
            "Please enter the directory you want to select as an absolute path:\n"
        )
        while not os.path.exists(directory):
            directory = input(
                "Please enter an existing directory you want to select as an absolute path:\n"
            )
        fileExt = "." + input(
            "Please enter the file extension of which you want be arranged ( * for all):\n"
        ).lstrip(" .")

        files = os.listdir(directory)
        files = list(map(lambda file: os.path.join(directory, file), files))
        files = list(filter(lambda file: os.path.isfile(file), files))
        if fileExt != ".*":
            files = list(filter(lambda file: file.endswith(fileExt), files))
        # print(files)
        data = {}
        for file in files:
            ext = "." + file.split(".")[-1]
            try:
                data[ext] = data[ext] + 1
            except:
                data[ext] = 1
            try:
                os.rename(file, os.path.join(directory, str(data[ext]) + ext))
            except:
                pass
        print("\n\n\n\n\n")
    except:
        print('An errro Occured Let\'s try again')
