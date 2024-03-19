#loan salery or age
salary=int(input("Salary :"))
age=int(input(("Age :")))
if(salary>=20000 or age<=25):
    print("Eligible")
    loan=int(input("Amount"))
    if(loan<50000):
        print("Eligible")
    else:
        print("Not eligible") 
else:
    print("NOT Eligible")