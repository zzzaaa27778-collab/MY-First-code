data_input = {"python" : "90%","php" : "67%","js" : "30%"}
def my_wifes(**name) :
    print(f"I love {name}  ")
    for key,value in name.items() :
         print(f"I love {key} and her is : {value} ")
         data_input[key] =value
         
my_wifes(Ruqaia='99%',gta='50%')  
print(data_input)