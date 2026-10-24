myskills={
    'python':'90%',
    'PHP':'10%',
    'JS':'50%',
    'NODE.JS':'80%'
}
for skill, progress in  myskills.items() :
    print(f"{skill} >= {myskills[skill]}")
mymanagers={
    'Ahmad':{
                'mean':'90%',
                'Value' : '20%'
          }
,   'Yahya':{
                    'mean':'10%',
                    'Value' : '100%'
        
        
        
    }
        
}
for main_key,Value_key in mymanagers.items() :
    print(f"-{main_key} is progress Is :")
    for son_key,son_value in Value_key.items() :
        print(f"-{son_key}>={son_value}")