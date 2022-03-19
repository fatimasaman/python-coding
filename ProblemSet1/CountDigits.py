# Take the following as input.
# A number
# A digit
# Write a function that returns the number of times digit is found in the number. 
# Print the value returned.

num = int(input())
digit = int(input())
i = 0
count = 0
while num != 0:
    rem = num % 10
    if rem == digit:
        count += 1
    num = num // 10
print(count)
