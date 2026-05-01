b = input("Enter binary: ")
decimal = 0

for i in range(len(b)):
    decimal += int(b[i]) * (2 ** (len(b) - i - 1))

print("Decimal:", decimal)