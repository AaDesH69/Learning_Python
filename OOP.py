class Cloth:
    def __init__(self, color, price, issold, company):
        self.color = color
        self.price = price
        self.issold = issold
        self.company = company

    def info(self):
        print(f"You Have a {kapda.color} {kapda.company}, Which Cost ${kapda.price}.")

kapda = Cloth("Blue", 2000, False, "Nike")

kapda.info()
