# It was connecting a three class in a single class
class grandpa():
    def phone(self):
        print("Grandpa's phone")
class dad(grandpa):
    def money(self):
        print("Dad's Money")
class son(dad,grandpa):
    def laptop(self):
        print("son's laptop")
ram=son()
ram.laptop()
ram.money()

d1=dad()
d1.phone()