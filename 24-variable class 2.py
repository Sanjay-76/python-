# self=object instance
# It was an class variable
class phone:
    chargertype="C-type"
    def __init__(self,a,b):
        self.brand=a
        self.price=b
    def display(self):
        print("brand",self.brand)
        print("price",self.price)
        print("chargertype",self.chargertype)

phone.chargertype="B-Type"
samsung=phone("samsung","10000")
samsung.display()

vivo=phone("vivo","10000")
vivo.display()

oppo=phone("oppo","10000",)
oppo.display()
