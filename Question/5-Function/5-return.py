# Set s_usernme="EMC"s_password="123"
# Get input for uname and password.
# Create a function called validate.
# if uname and password matches the function should return true else false.
s_uname="EMC"
s_password="123"

uname=input("Enter:")
password=input("Enter:")

def validate():
    if(uname==s_uname and password==s_password):
        return True
    else:
        return False
a=validate()
print(a)