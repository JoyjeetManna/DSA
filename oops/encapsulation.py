class Car:
    def __init__(self,model,brand):
        self.__model=model
        self.brand=brand

    def get_model(self):
        return self.__model + " bhagg"

    
my_car=Car("Model S","Tesla")
print(my_car.brand,my_car.get_model())        