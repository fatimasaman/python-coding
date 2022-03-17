n = 29

flag = 0
i = 2
while i <= n-1:

    if n%i == 0:
        flag = 1
        break
    i += 1

if flag:  #means flag = 1
    print("Not Prime")

else:
    print("Prime")
