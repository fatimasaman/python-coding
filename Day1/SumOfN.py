#Print sum of N Natural Numbers taking N as input from the user

n = int(input("Enter n:"))

i=1
sum = 0
while i<=n:
    sum += i
    i += 1
print(sum)