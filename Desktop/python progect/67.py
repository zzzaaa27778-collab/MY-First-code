sad=open("yahya.txt","w")
sad.write("Hello world in 99\n")
sad.write("Hello world\n")
sad.write("Fucing  122 world\n")
sad.write("Hello every one 100\n"*1000)
sad.close()
print()




mylist=['Ahmad\n','saad\n','yahya\n']

sad=open("yahya.txt","a")
sad.write("ffffff\n\n\n\n\n\n")

sad.write("hhhhhhh\n")

sad.writelines(mylist)
sad.close()
thefile=open("yahya.txt","r")
lines=thefile.readlines()
for line in lines[1104:1113] :
    print(line.strip())
thefile.close()    
#print(thefile.tell())
#print(thefile.seek(1104))
#print(thefile.read(1104))
import os
os.remove("yahya.txt")