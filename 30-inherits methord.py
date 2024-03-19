# __init__ it was an simply to the constructor.Then it was an most importand
# because it was not a using the __init__ (or) obj2.display not used on that.
# super().__init__() it was call the class of a,b is used.
# super methord for using the parend methord
class a():
    def __init__(self):
        print("A")

    def display(self):
        print("class A")

class b(a):
    def __init__(self):
        super().__init__()
        print("B")
    def display(self):
        print("class B")

class c(b,a):
    def __init__(self):
        super().__init__()
        print("C")

    def display(self):
        print("class C")
obj2=c()
