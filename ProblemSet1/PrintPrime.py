# Take N as input. Print all prime numbers from 2 to N

num = 10
j = 2

while j <= num:
    i = 2
    is_prime = 1

    while i < j:
        if j % i == 0:
            is_prime = 0
            break
        i+=1
    if is_prime == 1:
        print(j)
    j+=1