from payment import Payment

class Cash(Payment):
    def __init__(self, id):
        super().__init__(id)
    
pago = Cash(1033767)
print(vars(pago))