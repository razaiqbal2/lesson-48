class computer:
    def __init__(self):
        self. __max_price=90000
    def display(self):
        print("Cost price is",self.__max_price)

    def setmaxprice(self,price):
        self.__max_price=price

com1=computer()
com1.display()

com1. __max_price=100000
com1.display()

com1.setmaxprice(100000)
com1.display()