class Krak :
    def __init__(self,name):
        self.__name=name
    def get_name(self)    :
        return self.__name
    def set_name(self,now_name):
        self.__name = now_name
obj = Krak("Yahya")
print(obj.get_name())
print(obj.set_name("Ahmad"))
print(obj.get_name())
        