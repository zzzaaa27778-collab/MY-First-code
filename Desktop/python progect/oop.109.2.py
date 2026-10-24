class Naroto :
    def __init__(self):
        self.name= "Naroto"
        self.energy=100
        self.skills="Rasingan"
    def __str__(self):
        return f"The hero name is {self.name} and his enargy is {self.energy} and the better skills is {self.skills}"
    def __len__(self):
        self.Theloves=["Hinata","Ramen","Jeraia","Kakashi"]
        if self.name in self.Theloves:
            print(f"{self.name} is loved")
        else :
            print(f"{self.name} is shit") 
            return len(self.Theloves)   
    def _bool__(self)   :
        return self.energy > 0
hero= Naroto()
print(hero)
print("-"*40)           
if hero:
            print("Is have a good chakra")  
else :
            print("Is dead")  
              
    