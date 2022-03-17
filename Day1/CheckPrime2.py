n = 27

nof = 0
i = 2
while i <= n-1:

    if n%i == 0:
        nof += 1
        #print(i)
        break #(it is optional -if coming in the code &  1 factor is encountered, it is not prime)
        
    i += 1
    

if nof==0:
    print("Prime")
else:
    print("Not Prime")

# This gives another method of flag 
