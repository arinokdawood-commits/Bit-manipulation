
with open("sample.txt", "w") as file:
    file.write("Hello, this is the first line ")

with open("sample.txt", "a") as file:
    file.write("This line is appended.\n")

with open("sample.txt", "r") as file:
    data = file.read()
    print("File content:\n", data)