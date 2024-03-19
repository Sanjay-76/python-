#Cound the number whitch are divisible by 3 and 5 range 1-100
divisible=0
for i in range(1,100):
    if(i%2==0):
        divisible=divisible+1
    if(i%5==0):
        divisible=divisible+1 
print(divisible)