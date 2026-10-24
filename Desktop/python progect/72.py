text="yahya"
def formatText(text):
    return f"- {text.strip().capitalize()} -"
print( formatText(text))
x=['yahya','ahmad','sam','fff']
mygrandplan=map(formatText,x)
print(mygrandplan)
for name in list(map(formatText,x))  :
    print(name)