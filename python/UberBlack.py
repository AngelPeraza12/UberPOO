from car import Car

class UberBlack(Car):
    typeCarAccepted = []
    seatsMaterial = []

    def __init__(self, name, document, email, password, passenger, typeCarAccepted, seatsMaterial):
        super().__init__(name, document, email, password, passenger)
        self.typeCarAccepted = typeCarAccepted
        self.seatsMaterial = seatsMaterial

# test que el super objeto Car funciona
#uber = UberBlack("Angel peraza", "1033767", "angel@gmail.com", "4561223*", 5, ["Mazda3"], ["leather"])
#print(vars(uber))