from payment import Payment

numberCard = int
ccv = int
date = str

class Card(Payment):
    def __init__(self, id, numberCard, ccv, date):
        super().__init__(id)
        self.numberCard = numberCard
        self.ccv = ccv
        self.date = date
    