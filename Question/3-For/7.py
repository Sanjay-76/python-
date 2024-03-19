# wrte a program to read 10 numbers from the keyboard and find their sum and average
a=[]
#[] it bunch of data store with apend
print("Enter 10 number :")
for i in range (11):
    num=int(input("enter a num :"+str(i+1)))
    #a.apend is used to collecting a data from a "num" to store in "a"
    a.append(num)
print(a)
# then find the average of sum
sum=0
for i in a:
    sum=sum+i
print(sum)