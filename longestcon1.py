n = int(input())
b = bin(n)[2:]
print(max(len(x) for x in b.split('0')))