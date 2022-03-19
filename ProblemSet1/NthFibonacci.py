"""
Take as input N, a number. 
Write a recursive function to calculate Nth Fibonacci. Target complexity is O(N)

"""
n = int(input())
sum = 0
x = 0
y = 1
i = 1
while i < n:
    sum = x + y
    x = y
    y = sum
    i += 1

print(sum)