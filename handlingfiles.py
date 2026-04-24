
f = open("data.txt", "r")
print(f.read())
f.close()

f = open("data.txt", "w")
f.write("Hello")
f.close()

f = open("data.txt", "a")
f.write("\nNew Line")
f.close()