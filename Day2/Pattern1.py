n = 5
row = 1
nst = n
while row <= n:
    cst = 1
    while cst <= nst:
        print("*",end = " ") # end to get the stars in same line in a row
        cst += 1 
    print()                  # to get the row in new line
    row += 1
    