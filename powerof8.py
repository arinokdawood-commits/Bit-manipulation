n = int(input("Enter number: "))

while n > 1:
    if n % 8 != 0:
        print("Not a power of 8")
        break
    n = n // 8
else:
    print("Power of 8")