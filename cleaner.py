import os

selection = input("Location: ")

paths = {
    "downloads": r"C:/Users/kyler/Downloads",
    "desktop": r"C:/Users/kyler/OneDrive/Desktop"
}

os.chdir(paths[selection])
files = os.listdir(paths[selection])
duplicateFiles = []


for i in range(0,len(files)):
    for j in range(0, 10):
        if ("(" + str(j) + ")") in files[i]:
            duplicateFiles.append(files[i])

print("DUPLICATE FILES: ")
for i in range(0, len(duplicateFiles)):
    print(f"\t{duplicateFiles[i]}")

input = input(f"Deleting {len(duplicateFiles)} duplicate files, are you sure? (y/n): ")

if (input == 'y'):
    for i in range(0, len(duplicateFiles)):
        if os.path.exists(duplicateFiles[i]):
            print(f"Deleting #{i+1}: {duplicateFiles[i]}")
            os.remove(duplicateFiles[i])
elif (input == 'n'):
    print("Closing")