n = int(input("Enter number: "))

rightmost = n & -n

print("Rightmost set bit value:", rightmost)