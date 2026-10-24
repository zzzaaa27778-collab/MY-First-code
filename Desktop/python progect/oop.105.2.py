class Member :
    def __init__(self,first_name,secound_name,last_name):
       if not isinstance(first_name,str) or not first_name.isalpha() :
           raise ValueError("This is not (str) : This should be (str)")
       if not isinstance(secound_name,str) or not secound_name.isalpha() :
           raise ValueError("This is not (str) : This should be (str)")
       if not isinstance(last_name,str) or not last_name.isalpha() :
           raise ValueError("This is not (str) : This should be (str)")
       self.fname= first_name
       self.sname= secound_name
       self.lname= last_name
       
       print(f"The first name {first_name} and the secound name is {secound_name} ,Finally {last_name}")
Member_one= Member ("Yahya","Billal","Ahmad")            
Member_two= Member("jon","mad","kill")             
Member_three= Member("9","gta 5","red 0")             