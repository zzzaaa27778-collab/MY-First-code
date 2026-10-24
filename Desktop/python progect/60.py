my_managers={'Ahmad':"90%",
             'Yahya':"100%",
             'sam':"59%",
             'gak' : "31%",
             'dd' : "0%",
             'ss' : "55%"
}
def The_managers(name):
    print(f"{name}")
    for name,value in my_managers.items() :
        print(f"Hello {name}>={value}")
The_managers(my_managers)    