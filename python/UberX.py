from car import Car

class UberX(Car):
    brand = str
    model = str

    def __init__(self, name, document, email, password, passenger, brand, model):
        super().__init__(name, document, email, password, passenger)
        self.brand = brand
        self.model = model

#test funcionamiento
#car = UberX("Angelperaza", "1033767", "angel@gmail.com", "4445566*", 4, "Chevrolet", "Onix 2020")
#print(vars(car))