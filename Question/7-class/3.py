# create a class called teacher 
# create a variable = name and register number using constructor 
#  create  a function called display the name and register number of the teacher
# create t1 and t2 object and pass the name and reg no value through object.
class teacher:
    def __init__(self,name,reg):
        self.name=name
        self.regno=reg    
    def display(self):
        print(self.name)    
        print(self.regno)
t1=teacher("thomus","1")
t2=teacher("john","2")

t1.display()
t2.display()
