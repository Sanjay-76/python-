#Cound the number of add and even numbers between 1 to 10 and print it.
even=0
add=0
for i in range(1,11):
    if(i%2==0):
        even=even+1
    else:
        add=add+1
print(add)
print(even)