class Car:
    def __init__ (self,brand,model):
        self.brand=brand
        self.model=model
    def Full(self):
        return f"{self.brand} {self.model}"

class Ev(Car):
    def __init__(self,brand,model,blife):
        super() .__init__(brand,model)
        self.blife=blife

my_ev=Ev("Tesla","V8","85kW")
print(my_ev.model,my_ev.brand,my_ev.blife)
print(my_ev.Full())


