n = 5
row = 1
nsp = n-1
nst = 1
while row <= n:
    csp = 1
    while csp <= nsp:
        print(" ", end = " ")
        csp += 1

    cst = 1
    while cst <= nst:
        if cst % 2 != 0:
            print("*", end = " ")
        else:
            print(" ", end = " ")
        cst += 1 

    print()
    row += 1
    nsp -= 1
    nst += 2