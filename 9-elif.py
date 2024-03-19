#
mark=int(input("Score:"))
if(mark<35):
    print("Poor")
elif(mark>35 and mark<75):
    print("Average")
elif(mark>70 and mark<100):
    print("Good")
else:
     print("invalid")