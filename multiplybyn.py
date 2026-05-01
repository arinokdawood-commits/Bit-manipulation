a = int(input("Enter number: "))
n = int(input("Enter n: "))

result = a
print("1 iteration:", result)

for i in range(2, n+1):
    result = result * a

print("N iteration:", result)