from account import Account

class User(Account):
    def __init__(self, name, document, email, password):
        super().__init__(name, document, email, password)


user1 = User("Angel", "1033765575", "angel@gmail.com", "anglll44*")
print(vars(user1))

user2 = User("Kimberly lopez", "1033788888", "kim@gmail.com", "kiann22*")
print(vars(user2))
