myclass={ 
'math':'90%' ,
'English':'95%','TK':'80%',
'python':'99%','PHP':'29%',
'JS':'10%'
}
print(myclass['TK'])
        
for class_name in myclass :
    if int(myclass[class_name].replace('%','')) %2==0 :
        print(f"The class {class_name} and its score is {myclass[class_name]}is Event")   
    else :
        print(f"The class {class_name} and its score is {myclass[class_name]}is add")     