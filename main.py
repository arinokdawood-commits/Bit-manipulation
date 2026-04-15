# Program to check if a number i the power of 2

def power2(number):
    if(number == 0):
        return 0
    if((number & (~(number -1))) == number):
        return 1
    return 0
number = int(input("Enter the number :"))

if (power2(number)):
    print("\n The number i power of 2")
else:
    print("\nThe number os not power of 2")