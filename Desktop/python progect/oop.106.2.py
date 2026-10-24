class Member():
    def __init__(self,first_name,second_name,last_name,gender):
      self.fname=first_name
      self.sname=second_name
      self.lname=last_name
      self.gender = gender
    def full_name(self) :
          return f"{self.fname} {self.sname}, {self.lname}"
    def name_with_title(self):
        if self.gender == "Male" :
         return f"Welcome Mr.{self.fname}"
        elif self.gender=="Female" :
          return  f"Welcome Ms. :  {self.fname}"
        else:
            return f"Welcome :  {self.fname}"
member_one=Member("Yahya","sdd","asdf","Male")        
member_two=Member("ff/gfs000","we12r54","yyit","Female")        
member_three=Member("#$%&a","sd6969","d'f","Female")   
print(member_one.name_with_title())
print(member_one.full_name())   
print(member_two.name_with_title())  
    