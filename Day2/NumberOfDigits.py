# Print the number of digits of an integer given by the user

num = int(input())
nod = 0

while num != 0:
    num = num//10
    nod+=1
print(nod)  

#There is another way of doing it 
