class Car:
    def __init__(self,model,brand):
        self.model=model
        self.brand=brand
    #Functionality
    def full_name(self):
        return f"{self.model} {self.brand}"



my_car=Car("Tesla","V8")
print(my_car.model)
print(my_car.brand)
print(my_car.full_name())

my_car2=Car("Maruti","Suzuki")
print(my_car2.model)
print(my_car2.brand)
print(my_car2.full_name())


        
        
        
        
        
                 

        