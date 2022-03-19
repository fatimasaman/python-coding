''' 
Take the following as input.

A number (N1)
A number (N2)
Write a function which returns the LCM of N1 and N2. Print the value returned
'''

n1 = int(input())
n2 = int(input())

if n1 > n2:
    i = n1
else:
    i = n2

num = n1*n2
while i <= num:
    if (i % n1 == 0 and i % n2 == 0):
        print (i)
        break
    i += 1