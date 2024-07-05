import os

try:
    name = input("Enter file name with extension: ")
    files = os.listdir()
    if name in files:
        print(f"File '{name}' exists, nuv happy nega")
    else:
        raise FileNotFoundError(f"File '{name}' not found, inderect ga ledhu ani chptundhi man")
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print(e)
    print("Poyedhi em ledhu malli try chey")
