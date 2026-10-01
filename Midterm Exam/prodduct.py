class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price          
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value <= 0:
            raise ValueError("price must be greater than 0")
        self._price = value

    def total(self, qty):
        return self.price * qty


notebook = Product("Notebook", 25)
printer = Product("Print", 30)

print(printer.total(3))             # 90

try:
    printer.price = -30             # invalid price
except ValueError:
    print("rejected")
