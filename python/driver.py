from account import Account

class Driver(Account):
    def __init__(self, name, document, email, password):
        super().__init__(name, document, email, password)


driver1 = Driver("Katerine", "1033444789", "Katerine12@gmail.com", "K123456789*")
print(vars(driver1))

driver2 = Driver("Alejandro martinez", "24559987", "AlejandroM@gmail.com", "AlejandroMartinez/")
print(vars(driver2))