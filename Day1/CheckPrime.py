n = 28

nof = 0
i = 1
print("The factors of the number are:")
while i <= n:

    if n%i == 0:
        nof += 1
        print(i,end = " ") # gives the factors of the given number

    i += 1
print("\nThe number of factors are", nof)

if nof==2:
    print("The number is Prime")
else:
    print("The number is Not Prime")

# Another method
# n = 28
# nof = 0
# i = 1
# while i <= n-1:

#     if n%i == 0:
#         nof += 1

#     i += 1

# if nof==2:
#     print("Prime")
# else:
#     print("Not Prime")