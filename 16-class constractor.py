class laptop:
    def __init__ (self):
      self.price=0
      self.ram=""
      self.processer=""
    def display(self):
        print("display")
hp=laptop()
hp.price=50000
hp.ram="8gb" 
print(hp.price)