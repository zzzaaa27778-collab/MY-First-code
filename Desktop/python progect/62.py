x=2
print(f"Hello you are {x}")
def key():
    
    global x
    x=1
    print(f"The variable value is {x}")
def one():
    x=4
    print(f"The  value is {x}")    
def zero():   
    print(f"{x}") 
key()    
zero()
one()