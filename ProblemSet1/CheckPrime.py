# Take as input a number N, print "Prime" if it is prime if not Print "Not Prime"

n = int(input())
i = 2 
flag = 0
while i <= n-1:
    if n%i == 0:
        flag = 1
        break
    i += 1
if flag == 1:
    print("Not Prime")
else:
    print("Prime")
