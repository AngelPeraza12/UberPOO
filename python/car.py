from account import Account

class Car(Account):
    id = int   
    driver = Account         
    passenger = int         

    def __init__(self, name, document, email, password, passenger):
       super().__init__(name, document, email, password)
       self.passenger = passenger
       
#test de la clase car               
#car = Car("Angel peraza", "1033767", "angel@gmail.com", "4561223*", 5)
#print(vars(car))