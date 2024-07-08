class car:
    def __init__(self,model):
        self.model = model
        

    def color(self):
        print("color is", self.model)


c = car("red")

c.color()

class name(car):
    def __init__(self, model, age):
        super().__init__(model)
        self.age = age
        print(self.age)


n = name("blue", 20)

n.color()
