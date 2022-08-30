n = 5

row = 1
nst = n

while row <= n:
    cst = 1
    while cst <= nst:
        if row == 1 or row == n or cst == 1 or cst == nst:
            print("*", end = " ")
        else:    
            print(" ", end = " ")
        cst += 1

    print()
    row += 1