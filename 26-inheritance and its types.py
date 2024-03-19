# inheritance : it is an two types-> (single,multi,multi-level inheritance)
class dad():
    def phone(self):
        print("dads phone")

class mom():
    def sweet(self):
        print("mom's sweet")

class son(dad,mom):        
    def laptop(self):
        print("son's laptop")

ram=son()
ram.phone()
ram.sweet()