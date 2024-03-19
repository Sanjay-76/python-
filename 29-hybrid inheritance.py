class dad():
    def Money(self):
        print("dad's money")
class importand():
    def land(self):
        print("importand land")
class son1(dad,importand):
    def so1(self):
        print("money1")
class son2(dad):
    def so2(self):
        print("money2")
class son3(dad):
    def so3(self):
        print("money3")
s2=son1()
s2.Money()
s2.land()