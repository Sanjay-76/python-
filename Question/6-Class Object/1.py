#
class laptop:
    price=0
    processer=""
    ram=""
    def __init__(self):
        print("demo")
    def display(self):
        print("display")
hp=laptop()
dell=laptop()
lenovo=laptop()

hp.price=50000
hp.processer="i5"
hp.ram="8gb"

dell.price=60000
dell.processer="i7"
dell.ram="16gb"

lenovo.price=70000
lenovo.processer="i8"
lenovo.ram="32gb"

print(hp.price,hp.processer,hp.ram)
print(dell.price,dell.processer,dell.ram)
print(lenovo.price,lenovo.processer,lenovo.ram)
#lenovo_price
#lenovo_ram
#lenovo_display
#lenovo_processer
#lenovo_mouse-pointer
