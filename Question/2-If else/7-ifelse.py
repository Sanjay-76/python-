# Get input for score int formate.score>70 then get the student information
score=int(input())
if(score>70):
    Name=str(input("Name :"))
    Department=input("Department :")
    Location=input("Location :")
    print("Eligible")
    print(Name,Department,Location)
else:
    print("Not Eligible")
