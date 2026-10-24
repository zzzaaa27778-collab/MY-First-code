class Semba:
    def __init__(self,name):
         self.__name=name
    @property
    def get_name(self):
        x=9
        return f"{x} is my number  {self.__name}"
    @get_name.setter
    def get_name(self,new_name):
        self.__name=new_name
obj=Semba("Yahya")
print(obj.get_name)
obj.get_name = "Ahmad" 
print(obj.get_name)