n = int(input("Enter number: "))

binary = bin(n)[2:]         
rev = binary[::-1]           

new_num = int(rev, 2)        

print("Binary:", binary)
print("Reversed:", rev)
print("New number:", new_num)