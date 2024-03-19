# self=object instance
# It was an instance variable
class phone:
    def __init__(self,a,b,c):
        self.brand=a
        self.price=b
        self.chargetype=c
    def display(self):
        print("brand",self.brand)
        print("price",self.price)
        print("chargertype",self.chargetype)

samsung=phone("samsung","10000","c-type")
samsung.display()

vivo=phone("vivo","10000","c-type")
vivo.display()

oppo=phone("oppo","10000","c-type")
oppo.display()
