project_a=None
numberoftries= 7
while numberoftries > 0 :
    try:
        qwer=input("The file name is:<>   ").strip()
        project_a = open(qwer,'r')
        print(project_a.read())
        print(f"This {qwer} good")
        print(f"You have {numberoftries}tries")
        break
    except Exception as o :
        print(f"Some thing is wrong!: {o}")
        numberoftries-=1    
else :
    print("You are agree in my grande plan")    
    
    
    