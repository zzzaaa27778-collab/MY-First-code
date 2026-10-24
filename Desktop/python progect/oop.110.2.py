class cars:
    def __init__(self,name):
        self.name=name
    def __str__(self):
        return f"I wana have a sex with ruqaia in my {self.name}"
class BMW(cars) :  
    def __init__(self, name , model):
        super().__init__(name)
        self.model = model
w=BMW("BMW",2029)   
print(w)
    
