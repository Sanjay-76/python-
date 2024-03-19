# thare is an three types static methord
class laptop:
    chargertype="c-type"
    def __init__(self):
        self.brand=""
        self.price=24

    def setprice(self,price):
        self.price=price

    def getprice(self):
        print(self.price)
        print(self.chargertype)
    @classmethod #It was mention the class for laptop.laptop.setchargertype(laptop) or @classmethod
    def setchargertype(cls):
        cls.chargertype="B-Type"
        print("b type")

    @staticmethod #It was mention the class for hp.info(laptop) or @staticmethod
    def info():
        print("thish is an laptop class")   
hp=laptop()
hp.setprice(200000)
hp.getprice()

laptop.setchargertype()

hp.info()