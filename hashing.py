N = int(input())
str = input()
L = list(str)
l = []
j = 1
for i in L:
    A = ord(i)-96
    a = A * 31**(j-1)
    l.append(a)
    j = j+1
print(sum(l) % 1234567891)



