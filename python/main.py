from car import Car
from account import Account

if __name__ == "__main__":
    car = Car("AMS234", Account("Andres Herera", "1033788999"))
    car.passenger = 4
    print(vars(car))
    print(vars(car.driver))

    car1 = Car("RSP456", Account("Camilo Barrera", "1033778599"))
    car1.passenger = 4
    print(vars(car1))
    print(vars(car1.driver))

    car2 = Car("ABC452", Account("Andrea Cardenas", "1020445789"))
    car2.passenger = 4
    print(vars(car2))
    print(vars(car2.driver))
