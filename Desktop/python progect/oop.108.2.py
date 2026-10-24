class School :
    student_num = 0
    def __init__(self,student_fname):
        self.student_fname=student_fname
        School.student_num+=1
        print(f"Welcome {self.student_fname} in my grande plan")
    @classmethod 
    def show_school_info(cls)   :
        return f"Total students in shool: {cls.student_num}"
    @staticmethod
    def school_rules():
        return "Rule:Hard work beats talent."
my_school =School("Yahya")
print(School.show_school_info())       
print(School.school_rules())       
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    