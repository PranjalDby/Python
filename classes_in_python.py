class Motor:
    def __init__(self,name,model) -> None:
        self.name = name
        self.model = model
    
    def print_Info(self):
        print(self.name +"\n"+ f"{self.model}")

# Inheritance
class Engine (Motor):

    def __init__(self,name,model,cc,capacity):
        super().__init__(name,model)
        self.cc = cc
        self.capacity = capacity
    def print_Info(self):
        print(self.capacity + self.cc)
        return super().print_Info()

morss_Garage = Engine('morss_Garage','ECC451',500,5000)
morss_Garage.print_Info()