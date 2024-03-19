#get input for score out of 100
#if score is <35 print "Poor"
#if score is >35 and <70 print "average"
#if score is >70 print "Good"
mark=int(input("Score:"))
if(mark<35):
    print("Poor")
if(mark>35 and mark<75):
    print("Average")
if(mark>75):
    print("Good")
