from car import Car
from account import Account
from user import User

if __name__ == "__main__":

    car = Car("AMS234", "Andres Herera")
    car.passenger = 4
    print(vars(car))
    print(vars(car.driver))

    user1 = User("Angel", "1033765575", "angel@gmail.com", "anglll44*")
