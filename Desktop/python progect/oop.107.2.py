class Member :
    users_num = 0
    pp=["Jas","jdj","ww"]
    def __init__(self,self_fname,self_sname,self_lname,garder):
        self. first_name=self_fname
        self.secund_name=self_sname
        self.last_name=self_lname
        self.garder_name=garder
        Member.users_num += 1
    def greet(self)   :
        if self.first_name in Member.pp: 
            raise ValueError("Name Not Allowed!")
        return f"Hello { self.first_name}--{ self.secund_name}_ _ _{ self.last_name}  oop  { self.garder_name}"
user1=Member("Yahya","ww","w23rt0","Male")   
print(user1.greet()) 
print(f"Total Users: {Member.users_num}")    
    
    