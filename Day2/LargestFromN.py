# Take n numbers from the user and print the maximum

n = int(input("Enter N: "))
max = int(input())
i = 2  #or i=1
while i<=n:  #and here it will be n-1
    x = int(input())
    if max < x:
        max = x
    i += 1

print("The maximum number is", max)







