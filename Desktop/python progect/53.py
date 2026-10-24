managers=["Ahmad","Yahya","gak","sam"]
skills=["PHP","python","JS"]
for name in managers :
     print(f"The manager name is {name} and the skills is {skills}")
managers={'Ahmad': {'PHP':'10%',
                        'python':'90%',
                        'JS':'50%'},
                 'Yahya': {'PHP':'88%',
                         'python':'90%',
                         'JS':'50%'},
                'gak' :  {'PHP':'99%',
                         'python':'11%',
                         'JS':'77%'},
              'sam' :  {'PHP':'44%',
                         'python':'16%',
                         'JS':'66%'}
         }  
for name in managers : 
  #   for skill in skills :
#       print(f"-{skill}")       
  print(f"The name is {name} and he have {skills}")                  
for skill in skills :
    # print(f"Their {skill} is good for {managers[name]} ")               
     print(f"Their {skill} is good for {managers [name][skill]} ")               
     print(f"{name}>= {managers [name][skill]} ")               
                  
        
   
                
        
        
        
        
        
        
    