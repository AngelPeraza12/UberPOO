from car import Car

if __name__ == "__main__":
    car = Car()
    car.license = "AMS234"
    car.driver = "Andres Hereera"
    car.passenger = 4
    print(vars(car))

    car2 = Car()
    car2.license = "AMS244"
    car2.driver = "Felipe Guerrero"
    car2.passenger = 4
    print(vars(car2))

    car3 = Car()
    car3.licence = "LtP122"
    car3.driver = "Karen peña"
    car3.passenger = 4
    print(vars(car3))
    
