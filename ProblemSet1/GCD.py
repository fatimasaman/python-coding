'''
Take the following as input.

A number (N1)
A number (N2)
Write a function which returns the GCD of N1 and N2. Print the value returned.
'''
n1 = int(input())
n2 = int(input())

if n1 < n2:
    i = n1
else:
    i = n2

while i >= 1:
    if (n1 % i == 0 and n2 % i == 0):
        print (i)
        break
    i -= 1
